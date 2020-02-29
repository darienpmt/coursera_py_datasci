#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 05:51:48 2019

@author: darienpmt
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.dates as dates

#reading the csv file
weather = pd.read_csv('fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv')

#convert weather data to celcius
weather['Data_Value'] = weather['Data_Value'] / 10

#all dates to datetime format
weather['Date'] =  pd.to_datetime(weather['Date'])

#separate columns for year and month-day
weather['Year'] = weather['Date'].dt.year
weather['Month-Day'] = weather['Date'].dt.strftime('%m-%d')

#remove leap days and ID column
weather = weather[weather['Month-Day'] != '02-29'].drop('ID', axis=1)

#group data by month-day so we can find the high/lows for each day
max_temp = weather[(weather.Year < 2015) & (weather['Element'] == 'TMAX')].groupby(['Month-Day'])['Data_Value'].max()
min_temp = weather[(weather.Year < 2015) & (weather['Element'] == 'TMIN')].groupby(['Month-Day'])['Data_Value'].min()

#record breaking days
weather = weather.merge(max_temp.reset_index(drop=False).rename(columns={'Data_Value':'Max_temp'}), on='Month-Day', how='left')
weather = weather.merge(min_temp.reset_index(drop=False).rename(columns={'Data_Value':'Min_temp'}), on='Month-Day', how='left')

#sorting by date makes data easier to read
weather = weather.sort_values('Date')

#you can use "df['col']" or "df.col" to query a column in pandas - I didn't know that
record_h = weather[(weather['Year'] == 2015) & (weather['Data_Value'] > weather['Max_temp'])]
record_l = weather[(weather.Year == 2015) & (weather.Data_Value < weather.Min_temp)]

#setting x-axis (only using days from 2015, so it doesn't really matter, could have used days from 2014), dtype = 'datetime64[D]' is saying that is saying that the ouput of the array will be datetime and the [D] specifies it will be days
date_index = np.arange('2015-01-01','2016-01-01', dtype = 'datetime64[D]')

plt.figure()

#line plot with days from 2015 on the x-axis and max/min temps on the y axis
plt.plot(date_index, max_temp, color = 'black' , linewidth = 1)
plt.plot(date_index, min_temp, color = 'black', linewidth = 1 ) 

plt.scatter(record_h.Date.values, record_h.Data_Value.values, color='red', s=8)
plt.scatter(record_l.Date.values, record_l.Data_Value.values, color='blue', s=8)  

# Set x and y limits
ax = plt.gca()
ax.axis(['2015/01/01','2015/12/31',-50,50])

# Set axis names and title
plt.xlabel('Date', fontsize=10)
plt.ylabel('Celsius', fontsize=10)
plt.title('Temperature in Ann Arbour, Michigan (2005-2015)', fontsize=12)

# Create legend and title
# loc=0 provides the best position for the legend
plt.legend(['Record high (2005-2014)','Record low (2005-2014)','Record breaking high in 2015','Record breaking low in 2015'],loc=0,frameon=False)

# Fill colour between highs and lows
# alpha adjusts darkness of the shade
ax.fill_between(date_index, max_temp, min_temp, facecolor='grey', alpha=0.25)

# Where you locate the major ticks
ax.xaxis.set_major_locator(dates.MonthLocator(bymonthday=15))

# What you put at the ticks
ax.xaxis.set_major_formatter(dates.DateFormatter('%b'))

plt.show()            
                   



