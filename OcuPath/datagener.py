import pathlib
from keras_preprocessing.image import ImageDataGenerator
from .dataframer import DataFramer


class DataGener(DataFramer):
    '''
    Builds on DataFramer to create the Image Data Generators
    '''
    def __init__(self, target, df=None) -> None:
        super().__init__()
        self.target = target
        self.df = self.set_df(df)
        self.im_data_gen = ImageDataGenerator(rescale=1. / 255.,
                                              validation_split=0.2,
                                              rotation_range=15,
                                              width_shift_range=0.2,
                                              height_shift_range=0.2,
                                              brightness_range=(0.8, 1.2),
                                              zoom_range=0.2,
                                              horizontal_flip=True,
                                              vertical_flip=True)

        self.train_gen = self.im_data_gen.flow_from_dataframe(
            dataframe=self.df,
            directory=pathlib.Path(self.impath),
            x_col="Image",
            y_col=self.target,
            subset="training",
            batch_size=16,
            seed=42,
            shuffle=True,
            class_mode="binary",
            target_size=(64, 64))

        self.valid_gen = self.im_data_gen.flow_from_dataframe(
            dataframe=self.df,
            directory=pathlib.Path(self.impath),
            x_col="Image",
            y_col=self.target,
            subset="validation",
            batch_size=32,
            seed=42,
            shuffle=True,
            class_mode="binary",
            target_size=(64, 64))

    def set_df(self, df=None):
        if df is None:
            df = self.make_final_df()
        self.df = df
        return self.df
