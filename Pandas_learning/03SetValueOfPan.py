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

df.iloc[2, 2] = 1111  # 以position来定位数据，修改第三行第三列的那个数据
print(df)
#              A   B     C   D
# 2013-01-01   0   1     2   3
# 2013-01-02   4   5     6   7
# 2013-01-03   8   9  1111  11
# 2013-01-04  12  13    14  15
# 2013-01-05  16  17    18  19
# 2013-01-06  20  21    22  23

df.loc['20130101', 'B'] = 2222  # 以标签来定位再修改数据
print(df)
#              A     B     C   D
# 2013-01-01   0  2222     2   3
# 2013-01-02   4     5     6   7
# 2013-01-03   8     9  1111  11
# 2013-01-04  12    13    14  15
# 2013-01-05  16    17    18  19
# 2013-01-06  20    21    22  23


# 注意对数据的修改会一直存在，为了更直观的了解各种效果，需要之前的操作加上注释
'''df[df.A > 4] = 0
print(df)
#             A     B  C  D
# 2013-01-01  0  2222  2  3
# 2013-01-02  4     5  6  7
# 2013-01-03  0     0  0  0
# 2013-01-04  0     0  0  0
# 2013-01-05  0     0  0  0
# 2013-01-06  0     0  0  0
'''
'''df.A[df.A > 4] = 0
print(df)
#             A     B     C   D
# 2013-01-01  0  2222     2   3
# 2013-01-02  4     5     6   7
# 2013-01-03  0     9  1111  11
# 2013-01-04  0    13    14  15
# 2013-01-05  0    17    18  19
# 2013-01-06  0    21    22  23
'''

df.B[df.A > 4] = 0
print(df)
#              A     B     C   D
# 2013-01-01   0  2222     2   3
# 2013-01-02   4     5     6   7
# 2013-01-03   8     0  1111  11
# 2013-01-04  12     0    14  15
# 2013-01-05  16     0    18  19
# 2013-01-06  20     0    22  23

# 对DataFrame加上一列，加上NAN
df['F'] = np.nan
print(df)
#              A     B     C   D   F
# 2013-01-01   0  2222     2   3 NaN
# 2013-01-02   4     5     6   7 NaN
# 2013-01-03   8     0  1111  11 NaN
# 2013-01-04  12     0    14  15 NaN
# 2013-01-05  16     0    18  19 NaN
# 2013-01-06  20     0    22  23 NaN

# 对DataFrame加上一列,这一列是自己指定的值
df['E'] = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20130101', periods=6))
# 注意这里要和原dataFrame的index要一致
print(df)
#              A     B     C   D   F  E
# 2013-01-01   0  2222     2   3 NaN  1
# 2013-01-02   4     5     6   7 NaN  2
# 2013-01-03   8     0  1111  11 NaN  3
# 2013-01-04  12     0    14  15 NaN  4
# 2013-01-05  16     0    18  19 NaN  5
# 2013-01-06  20     0    22  23 NaN  6