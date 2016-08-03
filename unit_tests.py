from csv_to_numpy import Reader
import numpy as np
import os
import unittest

class CSVToNumpyTestCase(unittest.TestCase):
    def test_test(self):
        self.path = os.path.dirname(os.path.abspath(__file__)) + "/baseball/all_star.csv"
        self.r = Reader(self.path)
        self.arr = self.r.getNumpyArray()
        self.assertTrue(self.arr.shape[0] ==5070)

if __name__ == '__main__':
    unittest.main()
