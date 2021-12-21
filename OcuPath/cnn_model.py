# Build a baseline model

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Flatten, Dropout, BatchNormalization
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.metrics import Recall, Precision
from tensorflow.keras import regularizers
from tensorflow.keras import optimizers

class CNN_Model():
    '''
    Builds the CNN Model
    '''
    def __init__(self) -> None:
        pass

    def build_model(self):
        '''
        Build multi-layer model with dense head layers
        '''
        self.model = Sequential()
        self.model.add(Conv2D(32, (7, 7), padding='same', input_shape=(64, 64, 3), activation='relu'))
        self.model.add(MaxPooling2D(pool_size=(2, 2)))
        self.model.add(Conv2D(64, (3, 3), padding='same', activation='relu'))
        self.model.add(Conv2D(64, (3, 3), activation='relu'))
        self.model.add(MaxPooling2D(pool_size=(2, 2)))
        self.model.add(Dropout(0.1))
        self.model.add(Flatten())

        self.model.add(Dense(64, activation='relu'))
        self.model.add(Dropout(0.15))
        self.model.add(Dense(32, activation='relu'))
        self.model.add(Dropout(0.15))
        self.model.add(Dense(10, activation='relu'))
        self.model.add(Dropout(0.2))
        self.model.add(Dense(8, activation='sigmoid'))

        self.model.compile(optimizers.RMSprop(learning_rate=0.001, decay=1e-6),
                    loss="binary_crossentropy",
                    metrics=["accuracy", Recall(), Precision()])
        return self.model
