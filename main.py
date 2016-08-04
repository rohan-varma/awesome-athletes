#the class where the action happens
import pandas as pd
import numpy as np
from db_interactor import DBInteractor
from preprocess import Preprocessor

if __name__ == '__main__':
    #create a DB interactor
    interactor = DBInteractor("batting")
    df = interactor.get_current_data_frame()
    arr = interactor.df_to_numpy_matrix()
    #don't forget to disconnect
    interactor.disconnect()
    #create a preprocessor to preprocess the data
    processor = Preprocessor(arr)
    processor.print_curr_arr()
    #print processor.get_shape()
    #after preprocessing the data, cluster it.



    #build a locality sensitive hash table
