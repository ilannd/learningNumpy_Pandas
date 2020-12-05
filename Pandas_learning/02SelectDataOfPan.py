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

print(df['A'])
print(df.A)  # 两种方法输出同样的效果
# 2013-01-01     0
# 2013-01-02     4
# 2013-01-03     8
# 2013-01-04    12
# 2013-01-05    16
# 2013-01-06    20
# Freq: D, Name: A, dtype: int32

print(df[0:3])
#             A  B   C   D
# 2013-01-01  0  1   2   3
# 2013-01-02  4  5   6   7
# 2013-01-03  8  9  10  11
print(df['20130102':'20130104'])
#              A   B   C   D
# 2013-01-02   4   5   6   7
# 2013-01-03   8   9  10  11
# 2013-01-04  12  13  14  15

# 有下面四种方式(loc,iloc,ix,boolean)对数据进行筛选
# select by label:loc  ，也能同时对行和列进行操作筛选
print(df.loc['20130102'])
# A    4
# B    5
# C    6
# D    7
# Name: 2013-01-02 00:00:00, dtype: int32

# 对行和列同时进行操作
print(df.loc[:, ['A', 'B']])
#              A   B
# 2013-01-01   0   1
# 2013-01-02   4   5
# 2013-01-03   8   9
# 2013-01-04  12  13
# 2013-01-05  16  17
# 2013-01-06  20  21
print(df.loc['20130102', ['A', 'B']])
# A    4
# B    5
# Name: 2013-01-02 00:00:00, dtype: int32


# select by position: iloc ,也能同时对行和列进行操作筛选
print(df.iloc[3])  # 打印出第四行的数据
# A    12
# B    13
# C    14
# D    15
# Name: 2013-01-04 00:00:00, dtype: int32
print(df.iloc[3, 1])
# 13
print(df.iloc[3:5, 1:3])
#              B   C
# 2013-01-04  13  14
# 2013-01-05  17  18
print(df.iloc[[1, 3, 5], 1:3])
#              B   C
# 2013-01-02   5   6
# 2013-01-04  13  14
# 2013-01-06  21  22


# mixed selection : ix  # 混用loc 和 iloc
print(df.ix[:3, ['A', 'C']])  # 对行用label进行筛选,对列用position 进行筛选
#             A   C
# 2013-01-01  0   2
# 2013-01-02  4   6
# 2013-01-03  8  10


# Boolean indexing
print(df)
#              A   B   C   D
# 2013-01-01   0   1   2   3
# 2013-01-02   4   5   6   7
# 2013-01-03   8   9  10  11
# 2013-01-04  12  13  14  15
# 2013-01-05  16  17  18  19
# 2013-01-06  20  21  22  23
print(df[df.A > 8])
#              A   B   C   D
# 2013-01-04  12  13  14  15
# 2013-01-05  16  17  18  19
# 2013-01-06  20  21  22  23