#Given an input array, this class preprocess the data
#Removes non-integer /invalid data through a projection
#Uses principal components analysis to represent data in lower dimensions
import numpy as np

class Preprocessor:
    def __init__(self, data_set):
        np.set_printoptions(threshold=np.inf)
        self.data = np.array(data_set)
        self.feature_names = self.data[0]

    def get_shape(self):
        return self.data.shape

    def get_feature_names(self):
        return self.feature_names

    def get_max_feature_values(data_set):
        pass

    def remove_missing_indices(self, vector):
        return -1


    def scale_data(self, vector):
        pass

    def print_curr_arr(self):
        print self.data
