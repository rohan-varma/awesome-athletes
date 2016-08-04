import pandas as pd
import sqlite3

pd.set_option('display.width', 1000)
pd.set_option('display.max_columns', 500)

con = sqlite3.connect("test.db")
df = pd.read_sql_query("SELECT * from batting", con)
print(len(df))
print(df.head())

con.close()
