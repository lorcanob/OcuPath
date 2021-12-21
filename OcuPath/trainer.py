from OcuPath.params import *
from OcuPath.datagener import DataGener
from OcuPath.cnn_model import CNN_Model
from sklearn.pipeline import Pipeline
from tensorflow.keras.metrics import Recall, Precision
from tensorflow.python.keras.metrics import accuracy
from sklearn.metrics import recall_score, precision_score, accuracy_score
import pandas as pd
import numpy as np




class Trainer():
    '''
    Trainer class to fit the model
    '''
    def __init__(self, target=None):
        self.data = None
        self.target = self.set_target(target)
        self.pipeline = None
        self.train, self.val = self.make_data_generator()

    def make_data_generator(self):
        '''
        Calls DataGener and returns the training and validation generators
        '''
        datagener = DataGener(target=self.target)
        self.train, self.val = datagener.train_gen, datagener.valid_gen
        return self.train, self.val


    def run(self):
        '''
        Fits our model
        '''
        STEP_SIZE_TRAIN=self.train.n//self.train.batch_size
        STEP_SIZE_VALID=self.val.n//self.val.batch_size
        cnn_model = CNN_Model()
        self.pipeline = cnn_model.build_model()
        self.pipeline.fit(self.train,
                            steps_per_epoch=STEP_SIZE_TRAIN,
                            validation_data=self.val,
                            validation_steps=STEP_SIZE_VALID,
                            epochs=10)

    def set_target(self, target=None):
        if target is None:
            self.target = COLLAPSER.keys()
        return self.target



if __name__ == "__main__":
    trainer = Trainer(['cataract'])
    trainer.run()
