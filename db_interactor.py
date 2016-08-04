import pandas as pd
import numpy as np
import sqlite3

class DBInteractor:
    #default constructor that produces a DataFrame of all the columns in the batting table
    def __init__(self, table_name="batting"):
        pd.set_option('display.width', 1000)
        pd.set_option('display.max_columns', 500)
        self.con = sqlite3.connect("test.db")
        self.df = pd.read_sql_query("SELECT * from " + table_name, self.con)

    #pass in a table name and produces the dataframe for all the columns there
    # def __init__(self, table_name):
    #     pd.set_option('display.width', 1000)
    #     pd.set_option('display.max_columns', 500)
    #     self.con = sqlite3.connect("test.db")
    #     self.df = pd.read_sql_query("SELECT * from " + table_name, self.con)

    def drop_useless_stuff(self, cols_to_drop):
        self.df = self.df.drop(cols_to_drop, axis=1)
        return self.df

    def get_as_matrix(self):
        return df.as_matrix()

    def load_data_frame_from_table(self, table_name="batting", complete_query="default"):
        pd.set_option('display.width', 1000)
        pd.set_option('display.max_columns', 500)
        self.con = sqlite3.connect("test.db")
        if(complete_query == "default"):
            self.df = pd.read_sql_query("SELECT * from " + table_name, self.con)
        else:
            self.df = pd.read_sql_query(complete_query, self.con)
        return self.df

    #get the current dataframe
    def get_current_data_frame(self):
        return self.df


    #get the current dataframe as a matrix
    def df_to_numpy_matrix(self):
        return self.df.values

    #call this when you're done with an instance of the database interactor. Don't have more than one DB connection open at once!
    def disconnect(self):
        self.con.close()
