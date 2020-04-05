#!/usr/bin/env python3
# Author James Jordan
# Investigating forest fires dataset


# ---------imports--------------------------------------------------------------
import sqlite3 # a part of the standard python library
import pandas as pd # from requirements.txt
import matplotlib.pyplot as plt # from requirements.txt
import numpy as np # from requirements.txt
import seaborn as sns # from requirements.txt
import datetime as dt # from requirements.txt

from subprocess import check_output # ??????


#----------Begin Code-----------------------------------------------------------
file = sqlite3.connect("/Users/jamesjordan/Documents/Data Science/Projects/data/forest_fires/FPA_FOD_20170508.sqlite")
data = pd.read_sql_query("SELECT * FROM fires", con= file)

data['DATE'] = pd.to_datetime(data['DISCOVERY_DATE'] - pd.Timestamp(0).to_julian_date(), unit='D')

# Converting to day of week
data['day_of_week'] = data['DATE'].dt.day_name()

# Converting to month of year
data['month'] = pd.DatetimeIndex(data['DATE']).month
data['month'] = data.month.replace([1,2,3,4,5,6,7,8,9,10,11,12], ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

lst = ['DATE', 'day_of_week', 'month', 'FIRE_YEAR', 'DISCOVERY_TIME', 'STAT_CAUSE_DESCR', 'STATE', 'FIRE_SIZE']
data_final = data[lst]

dow = data_final.groupby(['day_of_week']).size().reset_index(name = 'count').sort_values('count')

# Creating barplot
plt.figure(figsize=(14,5))
g = sns.barplot(data = dow, y = 'count', x = 'day_of_week')
plt.xlabel('Day of week')
plt.ylabel('Number of wildfire cases')
g.axes.set_title('Graph showing number of wildfire per day of week',fontsize=20)

print(list(data.columns))

# Fire Size vs States
lst_fire_size = ['FIRE_SIZE', 'STATE']
data_fire_size = data[lst_fire_size]

dow_fire_size = data_fire_size.groupby(['STATE']).size().reset_index(name = 'count').sort_values('count')

plt.figure(figsize=(20,8))
g_fire_size = sns.barplot(data = dow_fire_size, y = 'count', x = 'STATE')
plt.xlabel('State')
plt.ylabel('Number of wildfires')
g_fire_size.set_title('Number of Wildfires by State', fontsize=20)
plt.savefig('../Documents/states.png')
