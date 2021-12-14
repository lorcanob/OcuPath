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
            homepath = os.path.join('content', 'drive', 'MyDrive', 'Colab Notebooks', 'Ocular pathology', 'ODIR-5K')
        else:
            homepath = os.path.join('..', 'raw_data')
        return homepath

    def read_data(self, drive=False, file='full_df.csv'):
        '''
        Reads the csv file into a Pandas DataFrame and stores it as an attribute
        '''
        self.path = self.set_data_path(drive)
        self.data = pd.read_csv(os.path.join(self.path, file), index_col='ID')
        return self.data

    def get_human_df(self):
        '''
        Returns human readable dataframe of each eye, ready to be made 'model ready'
        '''
        if self.data:
            right_data = self.data[RIGHT_INFO].rename(columns=RIGHT_MAPPER)
            right_data[['Eye']] = 'Right'

            left_data = self.data[LEFT_INFO].rename(columns=LEFT_MAPPER)
            left_data[['Eye']] = 'Left'

            human_df = pd.concat((right_data, left_data)).drop_duplicates().sort_index()
            human_df.index.name = 'Patient ID'
            return human_df
        return None

    def get_key_list(self, frame, key_list=None):
        '''
        Parses through the Diagnostic Keywords Series to create an exhaustive
        list of all keyphrases, separated by commas
        '''
        if key_list == None:
            key_list = []
        for eye in frame:
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
        if self.data:
            left = self.data[['Left-Fundus']].values.squeeze()
            right = self.data[['Right-Fundus']].values.squeeze()
            return left, right
        return None

    def test(self):
        '''
        Test function to ensure that the class has reloaded when running in Jupyter
        '''
        print(TARGET_LIST[0])
