import os
import re
import numpy as np
import pandas as pd

from .params import *

class DataFramer():
    '''
    Class to transform and prepare the raw csv file into a format that is more useful
    '''
    def __init__(self) -> None:
        self.impath = self.set_image_path()
        self.data = self.read_data()
        self.final_df = self.make_final_df()

    def set_data_path(self, drive=False, notebook=True):
        '''
        Sets data path dependent on whether the data is being accessed locally
        or via Google Drive
        '''
        if drive:
            self.datapath = os.path.join('/content', 'drive', 'MyDrive', 'Colab Notebooks', 'Ocular pathology')
        else:
            if notebook:
                self.datapath = os.path.join('..', 'raw_data')
            else:
                self.datapath = 'raw_data'
        return self.datapath

    def set_image_path(self,
                       drive=False,
                       notebook=True,
                       dir='preprocessed_images'):
        '''
        Set image path by calling data path
        '''
        self.set_data_path(drive, notebook)
        self.impath = os.path.join(self.datapath, dir)
        return self.impath

    def read_data(self, drive=False, notebook=True, file='full_df.csv'):
        '''
        Reads the csv file into a Pandas DataFrame and stores it as an attribute
        '''
        self.set_data_path(drive, notebook)
        self.data = pd.read_csv(os.path.join(self.datapath, file), index_col='ID')
        return self.data

    def get_human_df(self, data=None):
        '''
        Returns human readable dataframe of each eye, ready to be made 'model ready'
        '''
        if data is None:
            data = self.data

        right_data = self.data[RIGHT_INFO].rename(columns=RIGHT_MAPPER)
        right_data[['Eye']] = 'Right'

        left_data = self.data[LEFT_INFO].rename(columns=LEFT_MAPPER)
        left_data[['Eye']] = 'Left'

        self.human_df = pd.concat((right_data, left_data)).drop_duplicates().sort_index()
        self.human_df.index.name = 'Patient ID'
        return self.human_df

    def get_model_df(self, df=None):
        '''
        Returns dataframe with string inputs binary encoded
        '''
        if df is None:
            df = self.human_df
        self.model_df = df.copy()
        self.model_df['Patient Sex'] = self.model_df['Patient Sex'].map(SEX_MAPPER)
        self.model_df['Eye'] = self.model_df['Eye'].map(EYE_MAPPER)
        self.model_df = self.model_df.rename(columns=MODEL_MAPPER)
        return self.model_df

    def get_wide_df(self, df=None):
        '''
        Returns wide dataframe with all sub-pathologies to be fed collapser
        '''
        if df is None:
            df = self.encode_paths()
        self.wide_df = self.remove_missing(df)
        self.wide_df = self.wide_df.sort_values(by=['Patient ID', 'Right Eye'])
        return self.wide_df

    def remove_missing(self, df=None):
        '''
        Removes instances of missing images for model_df
        '''
        if df is None:
            df = self.model_df
        true_images = os.listdir(self.impath)
        return df[df['Image'].isin(true_images)]

    def get_key_list(self, series, key_list=None):
        '''
        Parses through the Diagnostic Keywords Series to create an exhaustive
        list of all keyphrases, separated by commas
        Ensure to pass in a Series, as a DataFrame will return only the column title
        '''
        if key_list == None:
            key_list = []
        for eye in series:
            keywords = re.findall(r'([\w\-\s]+)', eye)
            for word in keywords:
                key_list.append(word.strip())
        self.key_list = list(set(key_list))
        self.key_list.sort()
        return self.key_list

    def extract_jpg_names(self, data=None):
        '''
        Uses the self.data attribute to extract the filenames for the left and
        right eye images for each patient
        '''
        if data is None:
            data = self.data
        left = data[['Left-Fundus']].values.squeeze()
        right = data[['Right-Fundus']].values.squeeze()
        return left, right

    def encode_paths(self, df=None, keyword_list=None):
        '''
        Returns a dataframe with disease keyphrases from Diagnostic Keywords One Hot Encoded.
        By default we use all the key words in Diagnostic Keywords
        '''
        if df is None:
            df = self.model_df
        if keyword_list is None:
            keyword_list = self.get_key_list(df['Diagnostic Keywords'])
        # Can also pass a list of specific key words
        # OHE output is a binary 0 and 1 as strings for the datagen
        for diagnostic in keyword_list:
            df[f'{diagnostic}'] = df['Diagnostic Keywords'].map(lambda x:'1' if x == diagnostic else '0')
        self.encoded_df = df
        return self.encoded_df

    def single_path_collapser(self, pathology, df=None):
        '''
        Returns a dataframe with an additional column for a given pathology that
        is True if any of the sub-pathologies are labelled as '1'
        '''
        if df is None:
            df = self.wide_df
        temp_df = df[COLLAPSER[pathology]].astype(int).astype(bool)
        df[pathology] = np.logical_or.reduce(temp_df, axis=1)
        return df

    def multi_path_collapser(self, df=None):
        '''
        Applies the single pathology collapser to all pathologies in our COLLAPSER dictionary
        '''
        if df is None:
            df = self.wide_df
        for key in COLLAPSER.keys():
            df = self.single_path_collapser(key, df)
        self.narrow_df = df
        return self.narrow_df

    def collapse_paths(self, df=None):
        '''
        Calls multi_path_collapser on the dataframe and returns the final dataframe
        to be fed to the model
        '''
        if df is None:
            df = self.multi_path_collapser()
        df[list(COLLAPSER.keys())] = df[COLLAPSER.keys()].replace({True: 1, False: 0})
        self.final_df = df[FINAL_COLS]
        return self.final_df

    def make_wide_df(self):
        '''
        Calls the above methods to create the prepared dataframe
        '''
        self.read_data()
        self.get_human_df()
        self.get_model_df()
        self.encode_paths()
        self.get_wide_df()
        return self.wide_df

    def make_final_df(self):
        '''
        Calls all relevant functions to turn the raw input dataframe into the final
        dataframe to be sent to the model
        '''
        self.make_wide_df()
        self.collapse_paths()
        return self.final_df

    def test(self):
        '''
        Test function to ensure that the class has reloaded when running in Jupyter
        '''
        print(TARGET_LIST[0])
