import pandas as pd
import numpy as np
import k_means_clustering
from sklearn.preprocessing import Normalizer
from db_interactor import DBInteractor
from preprocess import Preprocessor

if __name__ == '__main__':
    np.set_printoptions(threshold=np.inf)
    #create a DB interactor
    interactor = DBInteractor("season_batting")
    #gets the dataframe
    df = interactor.get_current_data_frame()
    #print(df)
    #df = df.drop(['yearID','stint','stint','teamID','lgId','HBP', 'playerID'], axis=1)
    arr_with_ids = interactor.df_to_numpy_matrix()
    cols = ['playerID', 'yearID']
    df = interactor.drop_useless_stuff(cols)
    #converts it to a numpy matrix
    arr = interactor.df_to_numpy_matrix()
    arr = arr.astype(float)
    #print arr
    #print arr
    #don't forget to disconnect
    interactor.disconnect()
    #create a preprocessor to preprocess the data
    #this doesn't do anything very useful right now

    p = Preprocessor(arr, df)
    arr = p.preprocess(arr)
    print arr
