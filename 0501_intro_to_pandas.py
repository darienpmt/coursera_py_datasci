#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 16:49:39 2020

@author: darienpmt
"""
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

#Series

"""Series are a one dimensional array-like object contain a seq of values and 
an associated array of labels called its index."""

obj = pd.Series([4, 7, -5, 3])
#print(obj)

#print(obj.values)
#print(obj.index) # like range(4)

"""Often we will want to create a Series with an index indentifying each data
point with a label."""

obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
#print(obj2)
#print(obj2.index)
#print(obj2['a'])

obj2['d'] = 6

#print(obj2[['c', 'a', 'd']])

#print(obj2[obj2 > 0])

#print(obj2 * 2)

#print(np.exp(obj2))

#print('b' in obj2)
#print('e' in obj2)

sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = pd.Series(sdata)

#print(obj3)

states = ['California', 'Ohio', 'Oregon', 'Texas']

obj4 = pd.Series(sdata, index=states)
#print(obj4)

#print(pd.isnull(obj4))
#print(pd.notnull(obj4))

# Series also has these as instance methods
#print(obj4.isnull())

#print(obj3 + obj4)

obj4.name = 'population'
#print(obj4.name)
obj4.index.name = 'state'
#print(obj4.index.name)

#print(obj)

obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']
#print(obj)

#DataFrams
"""Creating a DataFrame: the most common ways are from a dict of equal-lenght
lists or NumPy arrays"""

data = {'state': ['Ohio', 'Ohio', 'Ohio' , 'Nevada', 'Nevada', 'Nevada'], 
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}

frame = pd.DataFrame(data)

#print(frame.head())

#you can specify a sequence of columns to rearrange the DataFrame's columns
new_frame = pd.DataFrame(data, columns=['year', 'state', 'pop']) 
#print('\n')

#print(new_frame)

#passing a col that isn't contained in the dict, it appears with missing values
frame2 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'], 
                      index=['one', 'two', 'three', 'four', 'five', 'six'])

#print(frame2)

#accessing the cols of the df
#print(frame2.columns)

""" a col in a df can be retrieved as a Series either by dict-like notation or
by attribute"""

#print(frame2['state'])

#print(frame2.year)

""" rows are retrieved by position or name using loc attribute"""

#print(frame2.loc['three'])

""" cols can be modified by assignment"""
frame2['debt'] = 16.5

#print(frame2)


""" when assigning lists or arrays to a col, the value's lenght must match the
length of the df. If you assign a Series, its labels will be realigned exactly
to the df index"""

val = pd.Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])

frame2['debt'] = val

#print('\n')

#print(frame2)

frame2['debt'] = np.arange(6.)
#print('\n')
#print(frame2)

""" Assigning a col that doesn't exist will create a new col. The del keyword
will delete cols as with a dict"""

frame2['eastern'] = frame2.state == 'Ohio'

#print(frame2)

del frame2['eastern']
#print(frame2.columns)

""" form of data from nested dicts"""

pop = {'Nevada': {2001: 2.4, 2002: 2.9}, 
       'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}

frame3 = pd.DataFrame(pop)

#print(frame3)

""" you can transpose a df (swap rows and cols) with similar syntax to NumPy"""
#print(frame3.T)

""" the keys in the inner dicts are combined and sorted to form the index in
the result. This isn't true if an explicit index is specified"""
#print('\n')
new_frame3 = pd.DataFrame(pop, index=[2001, 2002, 2003])
#print(new_frame3)

pdata = {'Ohio': frame3['Ohio'][:-1], 'Nevada': frame3['Nevada'][:2]}
#print('\n')
#print(pd.DataFrame(pdata))

frame3.index.name = 'year'; frame3.columns.name = 'state'
#print('\n')
#print(frame3)
#print(frame3.values)
#print(frame2.values)

# index objects
""" index objs are responsible for holding the axis labels and other metadata
(like the axis names and labels). Any array of other sequence of labels you use
when constructing a Series or df is internally converted to an index"""

obj = pd.Series(range(3), index=['a', 'b', 'c'])

index = obj.index

#print(index)

#print(index[1:])

""" index objects are immutable, this makes it safer to share Index objects
among data structures"""

labels = pd.Index(np.arange(3))

#print(labels)

obj2 = pd.Series([1.5, -2.5, 0], index=labels)
#print(obj2)

#print(obj2.index is labels)

print(frame3)
print('\n')
print(frame3.columns)
print('Ohio' in frame3.columns)
print(2003 in frame3.index)
print('\n')
dup_labels = pd.Index(['foo', 'foo', 'bar', 'bar'])

print(dup_labels)







































