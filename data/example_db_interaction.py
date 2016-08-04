import pandas as pd
import numpy as np
import sqlite3
from db_interactor import DBInteractor

if __name__ == '__main__':
    i = DBInteractor("pitching") #optional table argument
    df = i.get_current_data_frame()
    print df
    print "converting to numpy matrix"
    arr = i.df_to_numpy_matrix()
    print arr
    i.disconnect()
