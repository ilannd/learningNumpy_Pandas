import numpy as np
import pandas as pd

# merging two df by key/keys.(may be used in database)


left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})
print(left)
#     A   B key
# 0  A0  B0  K0
# 1  A1  B1  K1
# 2  A2  B2  K2
# 3  A3  B3  K3

print(right)
#     C   D key
# 0  C0  D0  K0
# 1  C1  D1  K1
# 2  C2  D2  K2
# 3  C3  D3  K3

# one key

# 两个DataFrame 有相同的列key,基于key,将两个DataFrame合并在一起

res = pd.merge(left, right, on='key')  # 参数on 就是选择哪一个column来进行merge
print(res)
#     A   B key   C   D
# 0  A0  B0  K0  C0  D0
# 1  A1  B1  K1  C1  D1
# 2  A2  B2  K2  C2  D2
# 3  A3  B3  K3  C3  D3


# two keys
left1 = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                      'key2': ['K0', 'K1', 'K0', 'K1'],
                      'A': ['A0', 'A1', 'A2', 'A3'],
                      'B': ['B0', 'B1', 'B2', 'B3']})

right1 = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                       'key2': ['K0', 'K0', 'K0', 'K0'],
                       'C': ['C0', 'C1', 'C2', 'C3'],
                       'D': ['D0', 'D1', 'D2', 'D3']})
print(left1)
#     A   B key1 key2
# 0  A0  B0   K0   K0
# 1  A1  B1   K0   K1
# 2  A2  B2   K1   K0
# 3  A3  B3   K2   K1
print(right1)
#     C   D key1 key2
# 0  C0  D0   K0   K0
# 1  C1  D1   K1   K0
# 2  C2  D2   K1   K0
# 3  C3  D3   K2   K0

res1 = pd.merge(left1, right1, on=['key1', 'key2'])
# res1 = pd.merge(left1, right1, on=['key1', 'key2'],how='inner')
# 默认的方法时inner
print(res1)
#     A   B key1 key2   C   D
# 0  A0  B0   K0   K0  C0  D0
# 1  A2  B2   K1   K0  C1  D1
# 2  A2  B2   K1   K0  C2  D2


# how=['left','right','outer','inner']
res2 = pd.merge(left1, right1, on=['key1', 'key2'], how='outer')
print(res2)
#      A    B key1 key2    C    D
# 0   A0   B0   K0   K0   C0   D0
# 1   A1   B1   K0   K1  NaN  NaN
# 2   A2   B2   K1   K0   C1   D1
# 3   A2   B2   K1   K0   C2   D2
# 4   A3   B3   K2   K1  NaN  NaN
# 5  NaN  NaN   K2   K0   C3   D3
res3 = pd.merge(left1, right1, on=['key1', 'key2'], how='left')
print(res3)
#     A   B key1 key2    C    D
# 0  A0  B0   K0   K0   C0   D0
# 1  A1  B1   K0   K1  NaN  NaN
# 2  A2  B2   K1   K0   C1   D1
# 3  A2  B2   K1   K0   C2   D2
# 4  A3  B3   K2   K1  NaN  NaN
res4 = pd.merge(left1, right1, on=['key1', 'key2'], how='right')
print(res4)
#      A    B key1 key2   C   D
# 0   A0   B0   K0   K0  C0  D0
# 1   A2   B2   K1   K0  C1  D1
# 2   A2   B2   K1   K0  C2  D2
# 3  NaN  NaN   K2   K0  C3  D3


# indicator
df1 = pd.DataFrame({'coll': [0, 1], 'col_left': ['a', 'b']})
df2 = pd.DataFrame({'coll': [1, 2, 2], 'col_right': [2, 2, 2]})
print(df1)
#   col_left  coll
# 0        a     0
# 1        b     1
print(df2)
#    col_right  coll
# 0          2     1
# 1          2     2
# 2          2     2
res5 = pd.merge(df1, df2, on='coll', how='outer', indicator=True)
# give the indicator a custom name
print(res5)
#   col_left  coll  col_right      _merge
# 0        a     0        NaN   left_only
# 1        b     1        2.0        both
# 2      NaN     2        2.0  right_only
# 3      NaN     2        2.0  right_only

res6 = pd.merge(df1, df2, on='coll', how='outer', indicator='indicator_column')
print(res6)
#   col_left  coll  col_right indicator_column
# 0        a     0        NaN        left_only
# 1        b     1        2.0             both
# 2      NaN     2        2.0       right_only
# 3      NaN     2        2.0       right_only


# merged by index
left2 = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                      'B': ['B0', 'B1', 'B2']},
                     index=['K0', 'K1', 'K2'])

right2 = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                       'D': ['D0', 'D2', 'D3']},
                      index=['K0', 'K2', 'K3'])
print(left2)
#      A   B
# K0  A0  B0
# K1  A1  B1
# K2  A2  B2
print(right2)
#      C   D
# K0  C0  D0
# K2  C2  D2
# K3  C3  D3

res7 = pd.merge(left2, right2, left_index=True, right_index=True, how='outer')
print(res7)
#       A    B    C    D
# K0   A0   B0   C0   D0
# K1   A1   B1  NaN  NaN
# K2   A2   B2   C2   D2
# K3  NaN  NaN   C3   D3

res8 = pd.merge(left2, right2, left_index=True, right_index=True, how='inner')
print(res8)
#      A   B   C   D
# K0  A0  B0  C0  D0
# K2  A2  B2  C2  D2


# handle overlapping

boys = pd.DataFrame({'k': ['K0', 'K1', 'K2'], 'age': [1, 2, 3]})
girls = pd.DataFrame({'k': ['K0', 'K0', 'K3'], 'age': [4, 5, 6]})
res9 = pd.merge(boys, girls, on='k', suffixes=['_boy', '_girl'], how='inner')
# suffix就是后缀的意思，是相同的列名有所区分
print(boys)
#    age   k
# 0    1  K0
# 1    2  K1
# 2    3  K2
print(girls)
#    age   k
# 0    4  K0
# 1    5  K0
# 2    6  K3
print(res9)
#    age_boy   k  age_girl
# 0        1  K0         4
# 1        1  K0         5
