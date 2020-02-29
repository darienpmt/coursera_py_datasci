#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 06:52:09 2020

@author: darienpmt
"""
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# Summarizing a Computing Descriptive Statistics
""" pandas objects are equipped with a set of common mathematical and 
statistical methods. Most of these are reductions or summary statistics,
methods that extract a single value (like sum or mean) from a Series or a
Series of values from the rows or cols of a df. Compared with the similar
methods from on NumPy arrays, they have built-in handing for missing data"""

df = pd.DataFrame([[1.4, np.nan], [7.1, -4.5], [np.nan, np.nan],
                   [0.75, -1.31]], index=['a', 'b', 'c', 'd'],
                    columns=['one', 'two'])
""" callign df's sum method returns a Series containing the col sums"""
#print(df)
#print('\n')
#print(df.sum())
#print('\n')
#print(df.sum(axis='columns')) # could also write axis=1 to sum across col instead
#print('\n')

""" NA values are excluded unless the entire slice (row or col in this case)
is NA. This can be disabled with the skipna option."""
#print(df.mean(axis='columns', skipna=False))
#print('\n')

""" some methods, like idmin and idmax, return indirect statistics like the
index value where the min or max values are attained."""

#print(df.idxmax())
#print('\n')

""" other methods are accumulations"""

#print(df.cumsum())
#print('\n')

""" another type of method is neither a reuduction nor an accumulation. 
describe is one such example, producing mulitple summary statistics in one shot"""

#print(df.describe())

""" on non-numerica data, describe produces alternative summary statistics."""
obj = pd.Series(['a', 'a', 'b', 'c'] * 4)

#print(obj)
#print('\n')
#print(obj.describe())

# Covariance and Correlation

""" some summary statistics, like correlation and covariance, are computed from
pairs of arguments."""

#import pandas_datareader.data as web

#all_data = {ticker: web.get_data_yahoo(ticker)
            #for ticker in ['AAPL', 'IBM', 'MSFT', 'GOOG', 'AMZN']}

#price = pd.DataFrame({ticker: data['Adj Close']
                       #for ticker, data in all_data.items()})

#volume = pd.DataFrame({ticker: data['Volume']
                       #for ticker, data in all_data.items()})

#returns = price.pct_change()


#print(price)
#print('----------------')
#print(volume)
#print('----------------')
#print(returns.tail())

""" the corr method of Series computes the correlation of the overlapping,
non-NA, aligned-by-index values in two Series. Relatedly, cov computes the
covariance"""

#print(returns['MSFT'].corr(returns['IBM']))
#print('\n')
#print(returns['MSFT'].cov(returns['IBM']))
#print('\n')

""" since MSFT is a valid Python attribute, we can also select these cols 
using more concise syntax"""

#print(returns.MSFT.corr(returns.IBM))
#print('\n')
#print(returns.corr())
#print('\n')
#print(returns.cov())
#print('\n')

""" using df's corrwith method, you can compute pairwise correlations between
a df cols or rows with another Series or DataFrame. Passing a Series returns
a Series with the correlation values computed for each col:"""

#print(returns.corrwith(returns.IBM))
#print('\n')
""" passing a df computes the correlations of matching col names. Below 
computes correlations of percent changes with volume."""

#print(returns.corrwith(volume))
#print('\n')

""" passing axis='columns' does things row-by-row instead. In all cases, the
data points are aligned by label before the correlation is computed."""


# Unique values, value counts and membership

obj = pd.Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])

uniques = obj.unique()
uniques.sort()
print(uniques)

print(obj.value_counts())

""" the Series is sorted by value in descending order as a convenience.
value_counts is also available as a top-level pandas metho that can be used
with any array or sequence."""

print(pd.value_counts(obj.values, sort=False))

""" isin performs a vectorized set membership check and can be useful in
filtering a dataset down to a subset of values in a Series or col 









































