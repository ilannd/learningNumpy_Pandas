import numpy as np
import pandas as pd

# concatenating  包括concat(join=)和append

df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['a', 'b', 'c', 'd'])
df3 = pd.DataFrame(np.ones((3, 4)) * 2, columns=['a', 'b', 'c', 'd'])
# index为默认的0,1,2,,
# columns为自定义的
print(df1)
#      a    b    c    d
# 0  0.0  0.0  0.0  0.0
# 1  0.0  0.0  0.0  0.0
# 2  0.0  0.0  0.0  0.0
print(df2)
#      a    b    c    d
# 0  1.0  1.0  1.0  1.0
# 1  1.0  1.0  1.0  1.0
# 2  1.0  1.0  1.0  1.0
print(df3)
#      a    b    c    d
# 0  2.0  2.0  2.0  2.0
# 1  2.0  2.0  2.0  2.0
# 2  2.0  2.0  2.0  2.0


# 合并concat
res = pd.concat([df1, df2, df3], axis=0)  # 0表示竖向的合并,默认
print(res)
# 得出的结果index有问题，还是原来的index
#      a    b    c    d
# 0  0.0  0.0  0.0  0.0
# 1  0.0  0.0  0.0  0.0
# 2  0.0  0.0  0.0  0.0
# 0  1.0  1.0  1.0  1.0
# 1  1.0  1.0  1.0  1.0
# 2  1.0  1.0  1.0  1.0
# 0  2.0  2.0  2.0  2.0
# 1  2.0  2.0  2.0  2.0
# 2  2.0  2.0  2.0  2.0

res0 = pd.concat([df1, df2, df3], axis=0, ignore_index=True)
print(res0)
# 将index重新进行排序
#      a    b    c    d
# 0  0.0  0.0  0.0  0.0
# 1  0.0  0.0  0.0  0.0
# 2  0.0  0.0  0.0  0.0
# 3  1.0  1.0  1.0  1.0
# 4  1.0  1.0  1.0  1.0
# 5  1.0  1.0  1.0  1.0
# 6  2.0  2.0  2.0  2.0
# 7  2.0  2.0  2.0  2.0
# 8  2.0  2.0  2.0  2.0


res1 = pd.concat([df1, df2, df3], axis=1)  # 1表示横向的合并
print(res1)
#      a    b    c    d    a    b    c    d    a    b    c    d
# 0  0.0  0.0  0.0  0.0  1.0  1.0  1.0  1.0  2.0  2.0  2.0  2.0
# 1  0.0  0.0  0.0  0.0  1.0  1.0  1.0  1.0  2.0  2.0  2.0  2.0
# 2  0.0  0.0  0.0  0.0  1.0  1.0  1.0  1.0  2.0  2.0  2.0  2.0


# join ['inner','outer']
df4 = pd.DataFrame(np.ones((3, 4)) * 0, index=[1, 2, 3], columns=['a', 'b', 'c', 'd'])
df5 = pd.DataFrame(np.ones((3, 4)) * 1, index=[2, 3, 4], columns=['b', 'c', 'd', 'e'])
print(df4)
#      a    b    c    d
# 1  0.0  0.0  0.0  0.0
# 2  0.0  0.0  0.0  0.0
# 3  0.0  0.0  0.0  0.0
print(df5)
#      b    c    d    e
# 2  1.0  1.0  1.0  1.0
# 3  1.0  1.0  1.0  1.0
# 4  1.0  1.0  1.0  1.0

res2 = pd.concat([df4, df5], join='outer')  # 默认的是join='outer'
print(res2)
# 把没有的列用None进行填充
#      a    b    c    d    e
# 1  0.0  0.0  0.0  0.0  NaN
# 2  0.0  0.0  0.0  0.0  NaN
# 3  0.0  0.0  0.0  0.0  NaN
# 2  NaN  1.0  1.0  1.0  1.0
# 3  NaN  1.0  1.0  1.0  1.0
# 4  NaN  1.0  1.0  1.0  1.0

res3 = pd.concat([df4, df5], join='inner')
print(res3)
#      b    c    d
# 1  0.0  0.0  0.0
# 2  0.0  0.0  0.0
# 3  0.0  0.0  0.0
# 2  1.0  1.0  1.0
# 3  1.0  1.0  1.0
# 4  1.0  1.0  1.0


# join_axes

res5 = pd.concat([df4, df5], axis=1)
print(res5)
#      a    b    c    d    b    c    d    e
# 1  0.0  0.0  0.0  0.0  NaN  NaN  NaN  NaN
# 2  0.0  0.0  0.0  0.0  1.0  1.0  1.0  1.0
# 3  0.0  0.0  0.0  0.0  1.0  1.0  1.0  1.0
# 4  NaN  NaN  NaN  NaN  1.0  1.0  1.0  1.0

res4 = pd.concat([df4, df5], axis=1, join_axes=[df4.index])  # 按照df4的index进行合并
print(res4)
#      a    b    c    d    b    c    d    e
# 1  0.0  0.0  0.0  0.0  NaN  NaN  NaN  NaN
# 2  0.0  0.0  0.0  0.0  1.0  1.0  1.0  1.0
# 3  0.0  0.0  0.0  0.0  1.0  1.0  1.0  1.0


# append
res6 = df1.append(df2, ignore_index=True)
print(res6)
#      a    b    c    d
# 0  0.0  0.0  0.0  0.0
# 1  0.0  0.0  0.0  0.0
# 2  0.0  0.0  0.0  0.0
# 3  1.0  1.0  1.0  1.0
# 4  1.0  1.0  1.0  1.0
# 5  1.0  1.0  1.0  1.0

res8 = df1.append([df2, df3], ignore_index=True)  # 能加多个，组成列表就行
print(res8)
#      a    b    c    d
# 0  0.0  0.0  0.0  0.0
# 1  0.0  0.0  0.0  0.0
# 2  0.0  0.0  0.0  0.0
# 3  1.0  1.0  1.0  1.0
# 4  1.0  1.0  1.0  1.0
# 5  1.0  1.0  1.0  1.0
# 6  2.0  2.0  2.0  2.0
# 7  2.0  2.0  2.0  2.0
# 8  2.0  2.0  2.0  2.0

s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
res7 = df1.append(s1, ignore_index=True)
print(res7)
#      a    b    c    d
# 0  0.0  0.0  0.0  0.0
# 1  0.0  0.0  0.0  0.0
# 2  0.0  0.0  0.0  0.0
# 3  1.0  2.0  3.0  4.0
