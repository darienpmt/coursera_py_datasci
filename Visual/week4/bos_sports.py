#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 16:00:05 2019

@author: darienpmt
"""
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_excel('bos_sports.xlsx')

yr = data['YEAR']
pats = data['Patriots Win Precent']
celts = data['Celtics Win Precent']
sox = data['Red Sox Win Percent']
bru = data['Bruins Win Percent']

pch = data[['YEAR','pChamps']].dropna()
cch = data[['YEAR','cChamps']].dropna()
rch = data[['YEAR','rChamps']].dropna()
bch = data[['YEAR','bChamps']].dropna()

plt.figure(figsize = (10,10))

y = plt.scatter(pch['YEAR'], pch['pChamps'] , color='black', s=35)
plt.scatter(cch['YEAR'], cch['cChamps'], color='black', s=35)
plt.scatter(rch['YEAR'], rch['rChamps'], color='black', s=35)
plt.scatter(bch['YEAR'], bch['bChamps'], color='black', s=35)

plt.plot(yr, pats, color = 'black', linestyle = '--', linewidth = 1)
plt.plot(yr, celts, color = 'green', linestyle = '--', linewidth = 1 ) 
plt.plot(yr, sox, color = 'red' , linestyle = '--', linewidth = 1)
plt.plot(yr, bru, color = 'yellow', linestyle = '--', linewidth = 1 ) 

plt.plot(yr[21:], pats[21:], color = 'blue' , linewidth = 2)
plt.plot(yr[21:], celts[21:], color = 'green', linewidth = 2 ) 
plt.plot(yr[21:], sox[21:], color = 'red' , linewidth = 2)
plt.plot(yr[21:], bru[21:], color = 'yellow', linewidth = 2 ) 

ax = plt.gca()
ax.axis([1978,2020,0,1.1])

ax.text(2020.5, 0.75, 'Patriots', color = 'blue',fontsize=12)
ax.text(2020.5, 0.67, 'Red Sox', color = 'red', fontsize=12)
ax.text(2020.5, 0.6, 'Celtics', color = 'green', fontsize=12)
ax.text(2020.5, 0.52, 'Bruins', color = 'black', fontsize=12)
ax.text(2006.5, 1.02, '-------- Before Tom Brady', color = 'black', fontsize=11)

plt.xlabel('Year', fontsize=10)
plt.ylabel('Win %', fontsize=10)
plt.title('Boston Sports Before and After Tom Brady', fontsize=12)

ax.legend((1,y), ('x','Championship Won by Team'),frameon=None)

plt.show() 

