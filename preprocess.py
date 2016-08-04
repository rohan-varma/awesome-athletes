#Given an input array, this class preprocess the data
#Removes non-integer /invalid data through a projection
#Uses principal components analysis to represent data in lower dimensions
import numpy as np
import pandas as pd
class Preprocessor:
    def __init__(self, data_set, data_frame):
        np.set_printoptions(threshold=np.inf)
        self.data = np.array(data_set)
        self.feature_names = self.data[0]
        self.df = data_frame



    #get the shape of the data
    def get_shape(self):
        return self.data.shape

    #get the feature names
    def get_feature_names(self):
        return self.feature_names

    #goes through the dataset and returns the max feature values
    def get_max_feature_values(self, data_set):
        return data_set.max(axis=0)

    #returns a new vector that has the removes the "zero" indices
    def remove_missing_indices(self, vector):
        return -1

    # returns a new vector with string indices removed
    def remove_string_indices(self, vector):
        pass #already implemented

    def scale_data(self, data_set):
        maxes = self.get_max_feature_values(data_set)
        for x in xrange(data_set.shape[0]):
            for y in xrange(data_set.shape[1]):
                data_set[x][y] = (data_set[x][y])/maxes[y]
        return data_set
    def print_curr_arr(self):
        print self.data

    def get_data(self):
        return self.data


    def preprocess(self, data):
        pass
