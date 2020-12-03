import pandas as pd
import numpy as np

dates = pd.date_range('20130101', periods=6)  # period是周期的意思
print(dates)
# DatetimeIndex(['2016-01-01', '2016-01-02', '2016-01-03', '2016-01-04',
#                '2016-01-05', '2016-01-06'],
#               dtype='datetime64[ns]', freq='D')


df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])  # index是行的索引，columns是列的索引
print(df)
#              A   B   C   D
# 2013-01-01   0   1   2   3
# 2013-01-02   4   5   6   7
# 2013-01-03   8   9  10  11
# 2013-01-04  12  13  14  15
# 2013-01-05  16  17  18  19
# 2013-01-06  20  21  22  23


# 修改数据
df.iloc[0, 1] = np.nan
df.iloc[1, 2] = np.nan
print(df)
#              A     B     C   D
# 2013-01-01   0   NaN   2.0   3
# 2013-01-02   4   5.0   NaN   7
# 2013-01-03   8   9.0  10.0  11
# 2013-01-04  12  13.0  14.0  15
# 2013-01-05  16  17.0  18.0  19
# 2013-01-06  20  21.0  22.0  23


print(df.dropna(axis=0, how='any'))
# 对行进行操作，how='any'意思就是一行有任意一个nan就丢掉这一行，默认
# how='all'表示一行所有的数据都是nan，才丢掉这一行
#              A     B     C   D
# 2013-01-03   8   9.0  10.0  11
# 2013-01-04  12  13.0  14.0  15
# 2013-01-05  16  17.0  18.0  19
# 2013-01-06  20  21.0  22.0  23

print(df.dropna(axis=1, how='any'))  # 对列进行操作
#              A   D
# 2013-01-01   0   3
# 2013-01-02   4   7
# 2013-01-03   8  11
# 2013-01-04  12  15
# 2013-01-05  16  19
# 2013-01-06  20  23


print(df.fillna(value=0))  # 将DataFrame中的nan填充为0
#              A     B     C   D
# 2013-01-01   0   0.0   2.0   3
# 2013-01-02   4   5.0   0.0   7
# 2013-01-03   8   9.0  10.0  11
# 2013-01-04  12  13.0  14.0  15
# 2013-01-05  16  17.0  18.0  19
# 2013-01-06  20  21.0  22.0  23

# 有时数据量很大的时候，不清楚有哪些nan值，可以用下面这种方法
print(df.isnull())
#                 A      B      C      D
# 2013-01-01  False   True  False  False
# 2013-01-02  False  False   True  False
# 2013-01-03  False  False  False  False
# 2013-01-04  False  False  False  False
# 2013-01-05  False  False  False  False
# 2013-01-06  False  False  False  False

# 数据量更大的时候，一眼得到dataFrame有没有空值
print(np.any(df.isnull()) == True)
# A    False   # 这一列没有nan
# B     True   # 这一列有nan
# C     True
# D    False
# dtype: bool
