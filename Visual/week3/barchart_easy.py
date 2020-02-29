#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 10:26:07 2019

@author: darienpmt
"""

# Use the following data for this assignment:
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.stats import norm


np.random.seed(12345)

#generates the samepl
df = pd.DataFrame([np.random.normal(32000,200000,3650), 
                   np.random.normal(43000,100000,3650), 
                   np.random.normal(43500,140000,3650), 
                   np.random.normal(48000,70000,3650)], 
                  index=[1992,1993,1994,1995])

#finds the mean of each row and then puts the 4 means into a list
df['mean'] = df.mean(axis=1)
rmeans = df['mean'].tolist()

#sets the error bars for each year by finding the standard error of the mean by year and using 0.975 for 95% CI
margin_of_err = df.sem(axis = 1) * norm.ppf(0.975)
y_error = margin_of_err.tolist()

#sets the x-axis
years = ['1992','1993','1994','1995']
x_pos = [i for i, _ in enumerate(years)]

plt.figure()

bars = plt.bar(x_pos, rmeans, width = 1, yerr = y_error, capsize = 15.0)
plt.xticks(x_pos, years)
y = rmeans[1]
plt.axhline(y, color='yellow')
ax = plt.gca()
ax.set_title('Custom Visualization - Sampling')

for bar in bars:
    if bar.get_height() > y:
        bar.set_color('red')
    elif bar.get_height() == y:
        bar.set_color('white') 
    else:
        bar.set_color('blue') 
        
for bar in bars:
    bar.set_edgecolor("k")
    bar.set_linewidth(1)

plt.show()