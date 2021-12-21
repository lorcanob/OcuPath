from OcuPath.params import *
from OcuPath.datagener import DataGener
from OcuPath.cnn_model import CNN_Model
from sklearn.pipeline import Pipeline
from tensorflow.keras.metrics import Recall, Precision
from tensorflow.python.keras.metrics import accuracy
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.metrics import recall_score, precision_score, accuracy_score
import pandas as pd
import numpy as np




class Trainer():
    '''
    Trainer class to fit the model
    '''
    def __init__(self, target=None, epochs=10, early_stop=True, drive=False, notebook=True):
        self.data = None
        self.target = self.set_target(target)
        self.epochs = epochs
        self.train, self.val = self.make_data_generator(drive, notebook)
        self.es = self.set_callbacks(early_stop)
        self.pipeline = None

    def make_data_generator(self, drive, notebook):
        '''
        Calls DataGener and returns the training and validation generators
        '''
        datagener = DataGener(self.target, drive, notebook)
        self.train, self.val = datagener.train_gen, datagener.valid_gen
        return self.train, self.val

    def set_callbacks(self, early_stop):
        if early_stop:
            self.es = EarlyStopping(patience=5, restore_best_weights=True)
            return self.es
        return None

    def run(self, train=None, val=None, epochs=None, callbacks=None):
        '''
        Fits our model on training and validation generators
        '''
        if train is None:
            train=self.train
        if val is None:
            val = self.val
        if epochs is None:
            epochs = self.epochs
        if callbacks is None:
            callbacks = self.es

        STEP_SIZE_TRAIN=train.n//train.batch_size
        STEP_SIZE_VALID=val.n//val.batch_size
        cnn_model = CNN_Model()
        self.pipeline = cnn_model.build_model()
        self.pipeline.fit(train,
                            steps_per_epoch=STEP_SIZE_TRAIN,
                            validation_data=val,
                            validation_steps=STEP_SIZE_VALID,
                            epochs=self.epochs,
                            callbacks=callbacks)

    def set_target(self, target=None):
        if target is None:
            self.target = COLLAPSER.keys()
        return self.target



if __name__ == "__main__":
    trainer = Trainer(['cataract'])
    trainer.run()
