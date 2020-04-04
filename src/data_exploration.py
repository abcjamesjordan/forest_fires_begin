#!/usr/bin/env python3
# Author James Jordan
# Investigating forest fires dataset


import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import datetime as dt

# /Users/jamesjordan/Documents/Data Science/Projects/Forest Fires/data

file = sqlite3.connect("/Users/jamesjordan/Documents/Data Science/Projects/Forest Fires/data/FPA_FOD_20170508.sqlite")
data = pd.read_sql_query("SELECT * FROM fires", con= file)

data['DATE'] = pd.to_datetime(data['DISCOVERY_DATE'] - pd.Timestamp(0).to_julian_date(), unit='D')

# Converting to day of week
data['day_of_week'] = data['DATE'].dt.day_name()
print(data['day_of_week'])

# Converting to month of year
data['month'] = pd.DatetimeIndex(data['DATE']).month
data['month'] = data.month.replace([1,2,3,4,5,6,7,8,9,10,11,12], ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
print(data['month'])

for col in data.columns:
    print(col)
