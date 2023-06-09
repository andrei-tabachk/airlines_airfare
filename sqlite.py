# sqlite_demo.py

import sqlite3
import pandas as pd

from pathlib import Path

# use pandas to create dataframe based on csv data
df_airefare_decrease = pd.read_csv(r'C:\Users\andre\OneDrive\Documents\Columbia University - Class Work\Repositories\airlines_airfare\cleaned_data.csv')
filtered_airefare_decrease = df_airefare_decrease[df_airefare_decrease['Year'] == 2017]

# create a sqlite database and a connection to it
cnxn = sqlite3.connect('airfare_decrease.sqlite')

# insert your dataframes into that database
filtered_airefare_decrease.to_sql('airefare_decrease', cnxn, index=False)

cnxn.close()