#the class where the action happens
import pandas as pd
import numpy as np
import k_means_clustering
from db_interactor import DBInteractor
from preprocess import Preprocessor

if __name__ == '__main__':
    #create a DB interactor
    interactor = DBInteractor("season_batting")
    #gets the dataframe
    df = interactor.get_current_data_frame()
    print(df)
    #df = df.drop(['yearID','stint','stint','teamID','lgId','HBP', 'playerID'], axis=1)
    cols = ['playerID', 'yearID']
    df = interactor.drop_useless_stuff(cols)
    #converts it to a numpy matrix
    arr = interactor.df_to_numpy_matrix()
    #don't forget to disconnect
    interactor.disconnect()
    #create a preprocessor to preprocess the data
    #this doesn't do anything very useful right now

    print(arr)



    #build a locality sensitive hash table
