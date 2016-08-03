import csv
import numpy as np
class Reader:
    def __init__(self, path_to_file):
        self.file_name = path_to_file
        self.file = open(self.file_name)
        self.reader = csv.reader(self.file)

    def getNumpyArray(self):
        li = []
        for row in self.reader:
                li.append(row)
        arr = np.array(li)
        return arr
