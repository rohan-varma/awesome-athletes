#the class where the action happens
import pandas as pd
import numpy as np
from db_interactor import DBInteractor
from preprocess import Preprocessor

if __name__ == '__main__':
    interactor = DBInteractor("batting")
    df = interactor.get_current_data_frame()
    arr = interactor.df_to_numpy_matrix()
    interactor.disconnect()
    processor = Preprocessor(arr)
    print processor.get_shape()
