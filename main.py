#the class where the action happens
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
    #don't forget to disconnect
    interactor.disconnect()
    #create a preprocessor to preprocess the data
    #this doesn't do anything very useful right now

    p = Preprocessor(arr, df)
    # maxes = p.get_max_feature_values(arr)
    # print maxes
    # arr = arr.astype(float)
    # arr = p.scale_data(arr)
    #print p.get_average_feature_values(arr)
    # for x in xrange(arr.shape[0]):
    #     all_zero = True
    #     for y in xrange(arr.shape[1]):
    #         if arr[x][y] != 0:
    #             all_zero = False
    #     if all_zero:
    #         print "found array with all zeros"
    # print "done checking for zeros"
    arr = p.preprocess(arr)
    print arr
    num_zeros = 0
    num_instances = 0
    for x in xrange(arr.shape[0]):
        for y in xrange(arr.shape[1]):
            num_instances = num_instances + 1
            if arr[x][y] == 0:
                num_zeros = num_zeros + 1
            if arr[x][y] > 1:
                print "something got messed up"
    print num_zeros/float(num_instances)







    #build a locality sensitive hash table
