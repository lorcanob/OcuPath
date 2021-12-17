from OcuPath.params import *
from OcuPath.dataframer import DataFramer
from OcuPath.datagener import DataGener
from OcuPath.cnn_model import CNN_Model
from sklearn.pipeline import Pipeline
from tensorflow.keras.metrics import Recall, Precision
from tensorflow.python.keras.metrics import accuracy
from sklearn.metrics import recall_score, precision_score, accuracy_score
import pandas as pd
import numpy as np




class Trainer():
    def __init__(self,target):
        self.data = None
        self.target = target
        self.pipeline = None
        self.train = None
        self.val = None

    def make_dataframe(self):
        dataframer = DataFramer()
        df = dataframer.read_data()
        df = dataframer.get_human_df(data=df)
        df = dataframer.get_model_df(df=df)
        df = dataframer.encode_paths(df=df, keyword_list=self.target)
        self.data = dataframer.get_final_df(df=df)


    def make_datagenerator(self):
        datagener = DataGener(data=self.data, target=self.target)
        self.train, self.val = datagener.train_gen, datagener.valid_gen


    def run(self):
        STEP_SIZE_TRAIN=self.train.n//self.train.batch_size
        STEP_SIZE_VALID=self.val.n//self.val.batch_size
        cnn_model = CNN_Model()
        self.pipeline = cnn_model.build_model()
        self.pipeline.fit(self.train,
                            steps_per_epoch=STEP_SIZE_TRAIN,
                            validation_data=self.val,
                            validation_steps=STEP_SIZE_VALID,
                            epochs=10)


if __name__ == "__main__":
    trainer = Trainer(['cataract'])
    trainer.make_dataframe()
    trainer.make_datagenerator()
    trainer.run()
