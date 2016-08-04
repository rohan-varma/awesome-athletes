#the class where the action happens
import pandas as pd
import numpy as np
from db_interactor import DBInteractor
from preprocess import Preprocessor

if __name__ == '__main__':
    #create a DB interactor
    interactor = DBInteractor("season_batting")
    #gets the dataframe
    df = interactor.get_current_data_frame()
    #converts it to a numpy matrix
    arr = interactor.df_to_numpy_matrix()
    #don't forget to disconnect
    interactor.disconnect()
    #create a preprocessor to preprocess the data
    #this doesn't do anything very useful right now
    processor = Preprocessor(arr, df)
    #processor.print_curr_arr()
    print processor.get_shape()
    #print processor.get_shape()
    #after preprocessing the data, cluster it.



    #build a locality sensitive hash table
