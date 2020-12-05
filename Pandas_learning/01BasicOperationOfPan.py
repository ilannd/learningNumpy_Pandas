import pandas as pd
import numpy as np

s = pd.Series([1, 3, 6, np.nan, 44, 1])  # nan就是None的意思，自动给列表加上了索引，而且还给出了数据的类型
print(s)
# 0     1.0
# 1     3.0
# 2     6.0
# 3     NaN
# 4    44.0
# 5     1.0
# dtype: float64


dates = pd.date_range('20160101', periods=6)  # period是周期的意思
print(dates)
# DatetimeIndex(['2016-01-01', '2016-01-02', '2016-01-03', '2016-01-04',
#                '2016-01-05', '2016-01-06'],
#               dtype='datetime64[ns]', freq='D')


df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=['a', 'b', 'c', 'd'])  # index是行的索引，columns是列的索引
print(df)
#                    a         b         c         d
# 2016-01-01  0.907509 -0.201774 -0.356775  1.267602
# 2016-01-02 -0.847316 -0.091822  0.277090  0.292777
# 2016-01-03  1.272314  1.922644 -0.410526  0.123373
# 2016-01-04 -0.612625  0.320317  1.863754 -0.763957
# 2016-01-05  1.247058  1.007385  1.090842  1.289759
# 2016-01-06  0.011876 -1.095806 -0.972253 -0.401769

# 用numpy导入数据来生成DataFrame
df1 = pd.DataFrame(np.arange(12).reshape((3, 4)))  # 未定义行和列的索引，默认是0 1 2....
print(df1)
#    0  1   2   3
# 0  0  1   2   3
# 1  4  5   6   7
# 2  8  9  10  11

# 用字典的方式定义DataFrame   其中index为默认值
df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})
print(df2)
#      A          B    C  D      E    F
# 0  1.0 2013-01-02  1.0  3   test  foo
# 1  1.0 2013-01-02  1.0  3  train  foo
# 2  1.0 2013-01-02  1.0  3   test  foo
# 3  1.0 2013-01-02  1.0  3  train  foo
print(df2.dtypes)
# A           float64
# B    datetime64[ns]
# C           float32
# D             int32
# E          category
# F            object
# dtype: object
print(df2.index)
# Int64Index([0, 1, 2, 3], dtype='int64')
print(df2.columns)
# Index(['A', 'B', 'C', 'D', 'E', 'F'], dtype='object')
print(df2.values)
# [[1.0 Timestamp('2013-01-02 00:00:00') 1.0 3 'test' 'foo']
#  [1.0 Timestamp('2013-01-02 00:00:00') 1.0 3 'train' 'foo']
#  [1.0 Timestamp('2013-01-02 00:00:00') 1.0 3 'test' 'foo']
#  [1.0 Timestamp('2013-01-02 00:00:00') 1.0 3 'train' 'foo']]
print(df2.describe())  # 只是会运算数值型的数据
#          A    C    D
# count  4.0  4.0  4.0
# mean   1.0  1.0  3.0
# std    0.0  0.0  0.0
# min    1.0  1.0  3.0
# 25%    1.0  1.0  3.0
# 50%    1.0  1.0  3.0
# 75%    1.0  1.0  3.0
# max    1.0  1.0  3.0
print(df2.T)

# 按照索引进行排序
print(df2.sort_index(axis=1, ascending=False))  # ascending=False表示倒序
#      F      E  D    C          B    A
# 0  foo   test  3  1.0 2013-01-02  1.0
# 1  foo  train  3  1.0 2013-01-02  1.0
# 2  foo   test  3  1.0 2013-01-02  1.0
# 3  foo  train  3  1.0 2013-01-02  1.0
print(df2.sort_index(axis=0, ascending=False))
#      A          B    C  D      E    F
# 3  1.0 2013-01-02  1.0  3  train  foo
# 2  1.0 2013-01-02  1.0  3   test  foo
# 1  1.0 2013-01-02  1.0  3  train  foo
# 0  1.0 2013-01-02  1.0  3   test  foo

# 也可以按照里面的值进行排序
print(df2.sort_values(by='E'))
#      A          B    C  D      E    F
# 0  1.0 2013-01-02  1.0  3   test  foo
# 2  1.0 2013-01-02  1.0  3   test  foo
# 1  1.0 2013-01-02  1.0  3  train  foo
# 3  1.0 2013-01-02  1.0  3  train  foo
