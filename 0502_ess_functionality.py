#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 14:42:02 2020

@author: darienpmt
"""
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# Reindexing

""" create a new object with the data conformed to a new index"""

obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
#print(obj)

""" calling reindex on this Series rearranges the data according to the
new index, introducing missing values if any index values were not already 
present"""
#print('\n')
obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
#print(obj2)

""" for ordered data like time series, it may be desireable to do some 
interpolation or filling of values when reindexing. The method option allows
us to do this, using a method such as ffill, which forward-fills the values"""

obj3 = pd.Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
#print(obj3)
#print('\n')

#print(obj3.reindex(range(6), method='ffill'))

""" with df, reindex can alter either the (row) index, col, or both.
When passed only a sequence, it reindexes the rows in the result."""

frame = pd.DataFrame(np.arange(9).reshape((3,3)), 
                               index=['a', 'c', 'd'],
                               columns=['Ohio', 'Texas', 'California'])
#print(frame)
#print('\n')
frame2 = frame.reindex(['a', 'b', 'c', 'd'])
#print(frame2)
"""cols can be reindexed with the colmns keyword"""
states = ['Texas', 'Utah', 'California']
#print('\n')
#print(frame.reindex(columns=states))
#print('\n')
""" you can reindex more succinctly by label-indexing with loc"""

foo = frame.loc[['a', 'b', 'c', 'd'], states]
#print(foo)
#print('\n')
foo['Utah'] = [i for i in range(4, 8)]
#print(foo)

# Dropping Entries from an Axis

obj = pd.Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
#print(obj)

new_obj = obj.drop('c')
#print(new_obj)

#print(obj.drop(['d', 'c']))

""" with df, index values can be deleted from either axis."""
data = pd.DataFrame(np.arange(16).reshape((4,4)),
                    index=['Ohio', 'Colorado', 'Utah', 'New York'],
                    columns=['one', 'two', 'three', 'four'])

#print(data)
#print('\n')
#print(data.drop(['Colorado', 'Ohio']))
#print('\n')
""" you can drop values from columns by passing axis=1 or axis='columns"""
#print(data.drop('two', axis=1))
#print('\n')
#print(data.drop(['two', 'four'], axis='columns'))

"""functions (like drop) which modify size or shape of a Series or df, can 
manipulate an object in-place without returning a new object"""

#print(obj)
#print('\n')
obj.drop('c', inplace=True)
#print(obj)

# indexing, selection and filtering

""" series indexing (obj[...]) works analogously to NumPy array indexing,
except you can use the Series index value instead of only integers"""

obj = pd.Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
#print(obj)
#print(obj['b'])
#print(obj[1])
#print(obj[2:4])
#print(obj[['b', 'a', 'd']])
#print(obj[[1,3]])
#print(obj[obj < 2])

"""slicing with labels behaves differently than normal Python slicing in that
the endpoint is inclusive"""

#print(obj['b':'c'])

""" setting using these methods modifies the corresponding section of the Series"""

obj['b':'c'] = 5

#print(obj)

""" indexing into a df is for retrieving one or more columns either with a 
single value or sequence"""

data = pd.DataFrame(np.arange(16).reshape((4,4)),
                    index=['Ohio', 'Colorado', 'Utah', 'New York'],
                    columns=['one', 'two', 'three', 'four'])
#print(data)

#print(data['two'])

#print(data[['three', 'one']])

"""indexing like this has a few speical cases. First, slicing or selecting
data with a boolean array"""

#print(data[:2])

#print(data[data['three'] > 5])

"""another use case is in indexing with a boolean DataFrame, such as one 
produced by a scalar comparison"""

#print(data < 5)

data[data < 5] = 0
#print(data)

# selection with loc and iloc
""" these enable you to select a subset of the rows and cols from a df with
NumPy type notation using either axis labels (loc) or integers (iloc)."""

#print(data)
#print('\n')
#print(data.loc['Colorado', ['two', 'three']])
#print('\n')
#print(data.iloc[2, [3, 0, 1]])
#print('\n')
#print(data.iloc[[1,2], [3, 0, 1]])
#print('\n')
"""both work with slices in addition to single labels or lists of labels"""
#print(data.loc[:'Utah', ['two', 'three']])
#print('\n')
#print(data.iloc[:, :3][data.three > 5])

#integer indexes
""" working with pandas objects indexed by integers is something often trips
up new users due to some differences with indexing semantics on built-in Python
data structures like lists and tuples. For example, you might not expect the
following to generate an error:"""

ser = pd.Series(np.arange(3.))

#print(ser)
#print(ser[-1]) #produces KeyError
#print('\n')
""" this is difficult because it's hard to know whether this is label-based
indexing or postion based indexing"""

"""with non-integer index, there is no potential for ambiguity"""
ser2 = pd.Series(np.arange(3.), index=['a', 'b', 'c'])
#print(ser2)
#print('\n')
#print(ser2[-1])
#print('\n')
"""if you have an axis index containing integers, data selection will always
be label-oriented. For more precise handling, use loc (for labels) or iloc
(for integers)"""

#print(ser[:1]) # not being precies
#print('\n')
#print(ser.loc[:1]) # using labels, both 0 and 1 are labels
#print('\n')
#print(ser.iloc[:1]) # using integers, FIRST row only (up to, not including 2nd row)

# Arithmetic for Data Alignment
""" when you are adding together objects, if any index pairs are not the same,
the respective index in the result will be the union of the index pairs. This
is similar to an automatic outer join on the undex labels."""

s1 = pd.Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'e'])

s2 = pd.Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a', 'c', 'e', 'f', 'g'])

#print(s1)
#print('\n')
#print(s2)
#print('\n')
#print(s1 + s2)

""" in the case of df, alignment is performed on both the rows and the cols"""
df1 = pd.DataFrame(np.arange(9.).reshape((3,3)), columns=list('bcd'),
                   index=['Ohio', 'Texas', 'Colorado'])

df2 = pd.DataFrame(np.arange(12.).reshape((4,3)), columns=list('bde'),
                   index=['Utah', 'Ohio', 'Texas', 'Oregon'])

#print(df1)
#print('\n')
#print(df2)

""" adding these returns a df whose index and cols are the unions of the ones
in each df"""

#print(df1 + df2)

df1 = pd.DataFrame({'A': [1, 2]})
df2 = pd.DataFrame({'A': [3, 4]})

""" if you add df objects with no column or row labels in common, the result
will contain all nulls"""

#print(df1)
#print('\n')
#print(df2)
#print('\n')
#print(df1 * df2)

# Arithmetic methods with fill values
""" in arithmetic operations between diferently indexed objects, you might want
to fill with a special value, like 0, when an axis label is found in one object
but not the other."""

df1 = pd.DataFrame(np.arange(12.).reshape((3, 4)), 
                   columns=list('abcd'))

df2 = pd.DataFrame(np.arange(20.).reshape((4, 5)),
                   columns=list('abcde'))

df2.loc[1, 'b'] = np.nan

#print(df1)
#print('\n')
#print(df2)
#print('\n')
#print(df1 + df2)
#print('\n')
#print(df1.add(df2, fill_value=0))
#print('\n')
#print(1 / df1)
#print(df1.rdiv(2))

""" whe reindexing a Series or df, you can also specify a different fill value"""
#print(df1.reindex(index = df2.index, columns=df2.columns, fill_value=0))

# operations between df and Series
arr = np.arange(12.).reshape((3,4))
#print(arr)
#print('\n')
#print(arr[0])
#print('\n')

""" when we subtract arr[0] from arr, the subtraction is performed once for 
each row. Thsi is referred to as Broadcasting. Operations between a df and a
Series are similar"""

#print(arr - arr[0])
#print('\n')

frame = pd.DataFrame(np.arange(12.).reshape((4, 3)),
                     columns=list('bde'),
                     index=['Utah', 'Ohio', 'Texas', 'Oregon'])

series = frame.iloc[0]

#print(frame)
#print('\n')
#print(series)

""" by default, arithmetic between df and Series matches the index of the Series
on the df's cols, broadcasting down the rows"""

#print(frame - series)
#print('\n')

""" if an index value is not found in either the df's cols or the Series's index
the objects will be reindexed to form the union"""

series2= pd.Series(range(3), index=['b', 'e', 'f'])

#print(frame + series2)
#print('\n')

""" if you want to instead broadcast over the cols, matching on the rows, you
have to use on of the arithmetic methods."""

series3 = frame['d']
#print(series3)
#print('\n')
#print(frame.sub(series3, axis='index'))

""" the axis number that you pass is the axis to match on. In this case we mean 
to match on the df's row index (axis='index' or axis=0) and broadcasting across"""

# Function Application and Mapping
""" NumPy's ufuncs (element-wise array methods) also work with pandas objects"""

frame = pd.DataFrame(np.random.randn(4, 3), columns=list('bde'),
                     index=['Utah', 'Ohio', 'Texas', 'Oregon'])

#print(frame)
#print('\n')
#print(np.abs(frame))
#print('\n')

""" another frequent operation is applying a function on one-dimensional
arrays to each column or row. df's apply method does exactly this."""

f = lambda x: x.max() - x.min() # takes max / min of a column

#print(frame.apply(f))
#print('\n')

""" here the function f, which computes the difference between the max and min
of a Series, is invoked one on each col in frame. The result is a Series
having the cols of frame as its index."""

""" if you pass axis='columns' to apply, the function will be invoked once per
row instead."""

#print(frame.apply(f, axis='columns'))
#print('\n')

""" many of the common array statistics (like sum and mean) are df methods,
so using apply is not necessary."""

""" the function passed to apply need not return a scalar value; it can also
return a Series with multiple values."""

def f(x):
    return pd.Series([x.min(), x.max(), x.mean()], index=['min', 'max', 'mean'])

#print(frame.apply(f))
#print('\n')
""" element-wise Python features can be used, too. Suppose you wanted to compute
a formatting string from each floating-point value in frame. You can do this
with apply map:"""

#format = lambda x: '%.2f' % x

#print(frame.applymap(format))
#print('\n')

""" the reason for the name applymap is that Series has a map method for 
applying an element-wise function."""

#print(frame['e'].map(format))

# Sorting and Ranking
""" sorting a dataset by some criterion is another important built-in 
operation. To sort lexiographically by row or col index, use the sort_index
method, which returns a new, sorted object."""

obj = pd.Series(range(4), index=['d', 'a', 'b', 'c'])

#print(obj.sort_index())

frame = pd.DataFrame(np.arange(8).reshape((2, 4)),
                     index=['three', 'one'],
                     columns=['d', 'a', 'b', 'c'])

#print(frame.sort_index())
#print('\n')
#print(frame.sort_index(axis=1))

""" data is sorted in ascending order by default, but can be sorted in 
descending order too"""
#print(frame.sort_index(axis=1, ascending=False))

""" to sort a Series by its values, use its sort_values method"""
obj = pd.Series([4, 7, -3, 2])

#print(obj.sort_values())
#print('\n')

""" missing values are sorted to the end of the Series by default"""

obj = pd.Series([4, np.nan, 7, np.nan, -3, 2])
#print(obj.sort_values())
#print('\n')

""" when sorting a df, you can use the data in one or more cols as the sort 
keys. To do so, pass one or more col nmaes to the by option of sort_values."""

frame = pd.DataFrame({'b': [4, 7, -3, 2], 'a': [0, 1, 0, 1]}) 

#print(frame)
#print('\n')
#print(frame.sort_values(by='b'))
#print('\n')

""" to sort by multiple cols, pass a list of names"""
#print(frame.sort_values(by=['a', 'b']))
#print('\n')
#print(frame.sort_values(by='a'))
#print('\n')

""" ranking assigns ranks from on through the number of valid data points in
any array. The rank methods for Series and df are the place to look; by 
default rank breaks ties by assigning each group the mean rank"""

obj = pd.Series([7, -5, 7, 4, 2, 0, 4])

#print(obj.rank())
#print('\n')

""" ranks can also be assigned according to the order in which they're observed
in the data"""

#print(obj.rank(method='first'))
#print('\n')

""" you can rank descending order too"""
# assign tie values the maximum rank in the group

#print(obj.rank(ascending=False, method='max'))

""" df can compute ranks over the rows or the cols"""
frame = pd.DataFrame({'b': [4.3, 7, -3, 2], 'a': [0, 1, 0, 1],
                      'c': [-2, 5, 8, -2.5]})

#print(frame)
#print('\n')
#print(frame.rank(axis='columns'))
#print('\n')
#print(frame.rank(axis='index'))

# Axis Indexes with Duplicate Labels

""" so far all index values (axis labels) have been unique. While many 
pandas functions (like reindex) require that the labels be unique, it's not
mandatory."""

obj = pd.Series(range(5), index=['a', 'a', 'b', 'b', 'c'])

#print(obj)
#print('\n')

""" index's is_unqiue property can tell you whether its labels are unique or
not"""

#print(obj.index.is_unique)
""" data selection is one of the main things that behaves differently with 
duplicates. Indexing a label with multiple entries returns a Series, while
single entries return a scalar value."""

#print(obj['a'])
#print('\n')
#print(obj['c'])

""" this can make your code more complicated, as the output type from indexing
can vary based on whether a label is repeated or not."""

""" the same logic extends to indexing rows in a df."""

df = pd.DataFrame(np.random.randn(4, 3), index=['a', 'a', 'b', 'b'])

#print(df)
#print('\n')
#print(df.loc['b'])
































































