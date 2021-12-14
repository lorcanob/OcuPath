import os
import re
import numpy as np
import pandas as pd

from .params import *

class DataFramer():
    def __init__(self) -> None:
        self.data = None

    def set_data_path(self, drive=False):
        if drive:
            homepath = os.path.join('content', 'drive', 'MyDrive', 'Colab Notebooks', 'Ocular pathology', 'ODIR-5K')
        else:
            homepath = os.path.join('..', 'raw_data')
        return homepath

    def read_data(self, drive=False, file='full_df.csv'):
        self.path = self.set_data_path(drive)
        self.data = pd.read_csv(os.path.join(self.path, file))
        return self.data

    def get_key_list(self, frame, key_list=None):
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
        if self.data:
            left = self.data[['Left-Fundus']].values.squeeze()
            right = self.data[['Right-Fundus']].values.squeeze()
            return left, right
        return None

    def test(self):
        print(TARGET_LIST[3])
