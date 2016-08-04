from csv_to_numpy import Reader
from preprocess import Preprocessor
import numpy as np
import os
import unittest

class CSVToNumpyTestCase(unittest.TestCase):
    def test_csv_to_numpy(self):
        self.path = os.path.dirname(os.path.abspath(__file__)) + "/baseball/all_star.csv"
        self.r = Reader(self.path)
        self.arr = self.r.getNumpyArray()
        self.assertTrue(self.arr.shape[0] ==5070)

class PreprocessTestCase(unittest.TestCase):
    def test_get_feature_names(self):
        feature_names = ["f1", "f2", "f3"]
        data_set = np.array([feature_names, ["1", "2", "3"], ["", "4", "5"]])
        preprocessor = Preprocessor(data_set)
        names = preprocessor.get_feature_names()
        self.assertTrue(feature_names[0] == names[0])
        self.assertTrue(feature_names[1] == names[1])
        self.assertTrue(feature_names[2] == names[2])

    def test_remove_missing_indices(self):
        arr = [1,2,3]
        p = Preprocessor(np.array(arr))
        self.assertTrue(p.remove_missing_indices(arr) == 5)

if __name__ == '__main__':
    unittest.main()
