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
        self.data = None

    def set_data_path(self, drive=False):
        '''
        Sets data path dependent on whether the data is being accessed locally
        or via Google Drive
        '''
        if drive:
            self.datapath = os.path.join('content', 'drive', 'MyDrive', 'Colab Notebooks', 'Ocular pathology')
        else:
            self.datapath = os.path.join('..', 'raw_data')
        return self.datapath

    def set_image_path(self, dir='preprocessed_images'):
        self.impath = os.path.join(self.datapath, dir)
        return self.impath

    def read_data(self, drive=False, file='full_df.csv'):
        '''
        Reads the csv file into a Pandas DataFrame and stores it as an attribute
        '''
        self.set_data_path(drive)
        self.data = pd.read_csv(os.path.join(self.datapath, file), index_col='ID')
        return self.data

    def get_human_df(self):
        '''
        Returns human readable dataframe of each eye, ready to be made 'model ready'
        '''
        if any(self.data):
            right_data = self.data[RIGHT_INFO].rename(columns=RIGHT_MAPPER)
            right_data[['Eye']] = 'Right'

            left_data = self.data[LEFT_INFO].rename(columns=LEFT_MAPPER)
            left_data[['Eye']] = 'Left'

            self.human_df = pd.concat((right_data, left_data)).drop_duplicates().sort_index()
            self.human_df.index.name = 'Patient ID'
            return self.human_df
        return None

    def get_model_df(self):
        '''
        Returns dataframe with string inputs binary encoded
        '''
        if any(self.human_df):
            self.model_df = self.human_df.copy()
            self.model_df['Patient Sex'] = self.model_df['Patient Sex'].map(SEX_MAPPER)
            self.model_df['Eye'] = self.model_df['Eye'].map(EYE_MAPPER)
            return self.model_df.rename(columns=MODEL_MAPPER)
        return None

    def remove_missing(self):
        '''
        Removes instances of missing images for model_df
        '''
        true_images = os.listdir(self.impath)
        self.model_df = self.model_df[self.model_df['Image'].isin(true_images)]
        return self.model_df

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
        key_list = list(set(key_list))
        key_list.sort()
        return key_list

    def extract_jpg_names(self):
        '''
        Uses the self.data attribute to extract the filenames for the left and
        right eye images for each patient
        '''
        if any(self.data):
            left = self.data[['Left-Fundus']].values.squeeze()
            right = self.data[['Right-Fundus']].values.squeeze()
            return left, right
        return None

    def test(self):
        '''
        Test function to ensure that the class has reloaded when running in Jupyter
        '''
        print(TARGET_LIST[1])
