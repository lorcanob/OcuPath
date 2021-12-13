import os
import re
import math
import numpy as np
import pandas as pd

class DataFramer():
    def __init__(self) -> None:
        pass

    def set_data_path(self, drive=True):
        if drive:
            homepath = os.path.join('content', 'drive', 'MyDrive', 'Colab Notebooks', 'Ocular pathology', 'ODIR-5K')
        else:
            homepath = os.path.join('..', 'raw_data')
        return homepath

    def read_data(self, path, file='full_df.csv'):
        data = pd.read_csv(os.path.join(path, file))
        return data

    def get_key_list(self, frame, key_list=None):
        if key_list == None:
            key_list = []
        for eye in frame:
            keywords = re.findall(r'([\w\-\s]+)', eye)
            for word in keywords:
                key_list.append(word.strip())
        return list(set(key_list))
