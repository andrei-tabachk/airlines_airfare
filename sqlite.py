# sqlite_demo.py

import sqlite3
import pandas as pd

from pathlib import Path

# use pandas to create dataframe based on csv data
df_airefare_decrease = pd.read_csv(r'C:\Users\andre\OneDrive\Documents\Columbia University - Class Work\Repositories\airlines_airfare\Consumer_Airfare_Report__Table_4_-_City-Pair_Markets_With_A_Substantial_Decrease_In_Average_Fare.csv')


# create a sqlite database and a connection to it
cnxn = sqlite3.connect('airfare_decrease.sqlite')

# insert your dataframes into that database
df_airefare_decrease.to_sql('airefare_decrease', cnxn, index=False)

cnxn.close()