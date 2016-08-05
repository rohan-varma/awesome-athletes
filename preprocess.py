#Given an input array, this class preprocess the data
#Removes non-integer /invalid data through a projection
#Uses principal components analysis to represent data in lower dimensions
import numpy as np
import pandas as pd
from sklearn.preprocessing import Normalizer

class Preprocessor:
    def __init__(self, data_set):
        np.set_printoptions(threshold=np.inf)
        self.data = np.array(data_set)
        self.feature_names = self.data[0]



    #get the shape of the data
    def get_shape(self):
        return self.data.shape

    #get the feature names
    def get_feature_names(self):
        return self.feature_names

    #goes through the dataset and returns the max feature values
    def get_max_feature_values(self, data_set):
        return data_set.max(axis=0)

    def get_average_feature_values(self, data_set):
        return np.mean(data_set, axis = 0)

    # returns a new vector with string indices removed
    def remove_string_indices(self, vector):
        pass #already implemented

    def scale_data(self, data_set):
        maxes = self.get_max_feature_values(data_set)
        avgs = self.get_average_feature_values(data_set)
        for x in xrange(data_set.shape[0]):
            for y in xrange(data_set.shape[1]):
                data_set[x][y] = (data_set[x][y])/maxes[y]
        return data_set

    def print_curr_arr(self):
        print self.data

    def get_data(self):
        return self.data

    def normalize(self, data):
        scaler = Normalizer().fit(data)
        data = scaler.transform(data)
        return data

    def remove_all_zeros(self, data):
        new_data = []
        for x in xrange(data.shape[0]):
            is_all_zeros = True
            for y in xrange(data.shape[1]):
                if data[x][y] != 0:
                    is_all_zeros = False
            if not is_all_zeros:
                new_data.append(data[x])
        data = np.array(new_data)
        return data

    def preprocess(self, data):
        #data = self.scale_data(data)
        #data = pca(data)
        data = self.remove_all_zeros(data)
        data = self.scale_data(data)
        return self.normalize(data)

