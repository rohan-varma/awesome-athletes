import csv
import numpy as np
class Reader:
    def __init__(self, path_to_file):
        np.set_printoptions(threshold=np.inf)
        self.file_name = path_to_file
        self.file = open(self.file_name)
        self.reader = csv.reader(self.file)
        self.li = []

    def getNumpyArray(self):
        for row in self.reader:
                self.li.append(row)
        arr = np.array(self.li)
        print arr[5000][7]
        return arr

    def getData(self):
        if(len(self.li) == 0):
            for row in self.reader:
                self.li.append(row)
        return self.li
