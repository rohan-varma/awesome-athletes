#the class where the action happens
import pandas as pd
import numpy as np
import k_means_clustering
from db_interactor import DBInteractor
from preprocess import Preprocessor

if __name__ == '__main__':
    #np.set_printoptions(threshold=np.inf)
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
    #print arr
    #don't forget to disconnect
    interactor.disconnect()
    #create a preprocessor to preprocess the data
    #this doesn't do anything very useful right now

    p = Preprocessor(arr, df)
    maxes = p.get_max_feature_values(arr)
    print maxes
    arr = arr.astype(float)
    arr = p.scale_data(arr)
    for x in xrange(arr.shape[0]):
        for y in xrange(arr.shape[1]):
            if arr[x][y] > 1:
                print "something got messed up"
    print "all good"



    #build a locality sensitive hash table
