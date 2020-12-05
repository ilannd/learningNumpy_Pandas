import numpy as np

# 不要把文件名命名为numpy

a = np.arange(3, 15)
print(a)
print(a[3])

a1 = np.arange(3, 15).reshape((3, 4))
print(a1)
print(a1[2])  # 现在索引的是行数
print(a1[1][1])  # 现在是8的索引
print(a1[1, 1])  # 实现与上面一样的功能
# 与数组的操作还是有相似之处的
print(a1[1, :])  # 打印第二行的所有数  [ 7  8  9 10]
print(a1[:, 1])  # 打印第一列的所有数
print(a1[1, 1:3])  # 打印第二行上第二列到第三列的数 [8 9]
print(a1[:, :])  # 打印整个矩阵

for row in a1:
    print(row)
# [3 4 5 6]
# [ 7  8  9 10]
# [11 12 13 14]
for column in a1.T:
    print(column)
# [ 3  7 11]
# [ 4  8 12]
# [ 5  9 13]
# [ 6 10 14]
print(a1.flatten())  # 返回一个被改变的array
print(a1.flat)  # a1.flat是一个迭代器
# <numpy.flatiter object at 0x0000023A41EB89C0>
for item in a1.flat:
    print(item)