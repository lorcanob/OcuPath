import pathlib
from keras_preprocessing.image import ImageDataGenerator
from .dataframer import DataFramer


class DataGener(DataFramer):
    def __init__(self) -> None:
        super().__init__()
        self.data = self.make_final_df()
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
            dataframe=self.data,
            directory=pathlib.Path(self.impath),
            x_col="Image",
            y_col=self.key_list,
            subset="training",
            batch_size=16,
            seed=42,
            shuffle=True,
            class_mode="multi_output",
            target_size=(64, 64))

        self.valid_gen = self.im_data_gen.flow_from_dataframe(
            dataframe=self.data,
            directory=pathlib.Path(self.impath),
            x_col="Image",
            y_col=self.key_list,
            subset="validation",
            batch_size=32,
            seed=42,
            shuffle=True,
            class_mode="multi_output",
            target_size=(64, 64))
