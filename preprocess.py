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


    def drop_useless_stuff(self, cols_to_drop):
        self.df = self.df.drop(cols_to_drop, axis=1)
        return self.df

    def get_as_matrix(self):
        return self.df.as_matrix()


    #get the shape of the data
    def get_shape(self):
        return self.data.shape

    #get the feature names
    def get_feature_names(self):
        return self.feature_names

    #goes through the dataset and returns the max feature values
    def get_max_feature_values(self, data_set):
        pass
    #returns a new vector that has the removes the "zero" indices
    def remove_missing_indices(self, vector):
        return -1
    # returns a new vector with string indices removed
    def remove_string_indices(self, vector):
        pass

    def scale_data(self, vector):
        pass

    def print_curr_arr(self):
        print self.data

    def get_data(self):
        return self.data


    def preprocess(self, data):
        new_data_set = []
        for x in xrange(data.shape[0]):
            new_data_set.append(remove_missing_indices(remove_string_indices(data[x])))
