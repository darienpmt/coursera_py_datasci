#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 17:20:24 2019

@author: darienpmt
"""
import matplotlib.pyplot as plt
import pandas as pd

#reading the csv file
weather = pd.read_csv('fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv')

#convert weather data to celcius
weather['Data_Value'] = weather['Data_Value'] / 10

#all dates to datetime format
weather['Date'] =  pd.to_datetime(weather['Date'])

#separate columns for year and month-day
weather['Year'] = weather['Date'].dt.year
weather['Month-Day'] = weather['Date'].dt.strftime(%m - %d)

#remove leap days
weather = weather[weather['Month-Day'] == '02-29']

print(weather)



weather.index = pd.to_datetime(weather.index)
weather = weather[~((weather.index.month == 2) & (weather.index.day == 29))]

weatherlarge = weather[weather.index.year != 2015]
weathersmall = weather[weather.index.year == 2015]


weather_max = weatherlarge.groupby([(weatherlarge.index.month),(weatherlarge.index.day)]).max()
weather_min = weatherlarge.groupby([(weatherlarge.index.month),(weatherlarge.index.day)]).min()

weathersmall_max = weathersmall.groupby([(weathersmall.index.month),(weathersmall.index.day)]).max()
weathersmall_min = weathersmall.groupby([(weathersmall.index.month),(weathersmall.index.day)]).min()

max_lst = weather_max['Data_Value'].tolist()
min_lst = weather_min['Data_Value'].tolist()
lastyr_max = weathersmall_max['Data_Value'].tolist()
lastyr_min = weathersmall_min['Data_Value'].tolist()

plt.figure(figsize=(10,10))

maxcount = 0
mincount = 0
maxdays = []
mindays= []
maxtoplot = []
mintoplot = []

for x ,y in zip(lastyr_max, max_lst):
    maxcount += 1
    if x > y:
        maxdays.append(maxcount)
        maxtoplot.append(x)
        
for x, y in zip(lastyr_min, min_lst):
    mincount += 1
    if x < y:
        mindays.append(mincount)
        mintoplot.append(x)

x, y = zip(*list(zip(maxdays, maxtoplot)))
w ,z = zip(*list(zip(mindays, mintoplot)))
       
plt.scatter(x, y, c='red', label = '2015 Record High')
plt.scatter(w, z, c='blue',label = '2015 Record Low')


plt.plot(max_lst, '-k.', label = '2005-2014 Max')
plt.plot(min_lst, '-k.', label = '2005-2014 Min')
plt.gca().fill_between(range(len(max_lst)), max_lst, min_lst, facecolor='black', alpha=0.2)
ax = plt.gca()
plt.xlabel('Day of Year')
plt.ylabel('Temperature in Celcius')
plt.title('Maximum and Minium Daily Temperatures 2005-2014 vs. 2015')
plt.legend()

plt.show()