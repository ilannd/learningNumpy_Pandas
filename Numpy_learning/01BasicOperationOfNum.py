import numpy as np
# 不要把文件名命名为numpy

# 两行三列的矩阵
array = np.array([[1, 2, 3],
                  [2, 3, 4]])
print(array)
print('number of dim:', array.ndim)  # 数组的维数
print('shape:', array.shape)  # 数组的行列，以元组形式输出 (2, 3)
print('size:', array.size)  # 数组元素个数

a = np.array([2, 3, 4])  # 用列表的形式来创建
print(a)

b = np.array([2, 3, 4], dtype=np.int)  # np.float
# anaconda 应该默认装的30位的python
print(b.dtype)  # int32

c = np.zeros((3, 4))  # 默认浮点型
print(c)

d = np.ones((3, 4))  # 默认浮点型
print(d)
d1 = np.ones((3, 4), dtype=np.int)  # 指定类型为整数类型
print(d1)
print(d1.dtype)

e = np.empty((3, 4))  # 数据为随机产生的数据，但是我的运行结果全是1
print(e)

f = np.arange(10, 20, 2)  # 输出结果为[10 12 14 16 18]  是arange函数，不是arrange
print(f)
g = np.arange(12)
print(g)

g1 = np.arange(12).reshape((3, 4))  # 重新定义数组的形状
print(g1)

# linspace 等分
h = np.linspace(1, 10, 5)  # 前两个参数表示范围，最后一个参数表示多少段
print(h)
h1 = np.linspace(1, 10, 9)
print(h1)
h2 = np.linspace(1, 10, 6).reshape((2, 3))
print(h2)

# 数组的运算
i = np.array([10, 20, 30, 40])
i1 = np.arange(4)
i2 = i - i1  # 数组的减运算
i3 = i + i1
i4 = i1 ** 2  # 数组的次方运算，python的次方使用**来表示的
i5 = 10 * np.sin(a)  # cos(),tan()也一样
print(i, i1)
print(i1)  # i1的输出结果为[0 1 2 3]
print(i1 < 3)  # 数组的逻辑运算，输出结果为[ True  True  True False]
print(i1 == 3)  # 注意是==
print(i2)
print(i3)
print(i4)
print(i5)

# 矩阵的运算
j = np.array([[1, 1],
              [0, 1]])
j1 = np.arange(4).reshape((2, 2))
print(j)
print(j1)
# 逐个相乘,就是矩阵对应位置的元素相乘所得结果，比c11=a11*b11
j2 = j * j1
print(j2)
# 矩阵里面的乘法,现代里面的乘法
j3 = np.dot(j, j1)
j4 = j.dot(j1)  # 与上面一样的效果
j5 = j1.dot(j)  # 与上面运行结果不同，因为矩阵乘法不满足交换律
print(j3)
print(j4)
print(j5)

# 随机生成的矩阵,元素大小在0-1之间
k = np.random.random((2, 4))
print(k)
# 最大值，最小值，求和函数的调用
print(np.sum(k))
print((np.sum(k, axis=1)))  # 将每一行进行求和,对列向量进行操作
print((np.sum(k, axis=0)))  # 将每一列进行求和，对行向量进行操作
print(np.max(k, axis=0))  # 对每一列求最大值，对行向量进行操作
print((np.min(k, axis=1)))  # 对每一行求最大值，对列向量进行操作

l = np.arange(2, 14).reshape((3, 4))
print(np.argmin(l))  # l中最小值得索引
print(np.argmax(l))  # l中最大值的索引
print(np.mean(l))  # l的平均值
print(l.mean())  # 与上边一样的效果
print((np.average(l)))  # 与上边一样的效果
# print(l.average())  # 不能这样写，老版本可以，但新版本没更新，不能用
print(np.median(l))  # l的中位数
print(l)
# [[ 2  3  4  5]
#  [ 6  7  8  9]
#  [10 11 12 13]]
print(np.cumsum(l))  # 一种累加的效果，[ 2  5  9 14 20 27 35 44 54 65 77 90]
print(np.diff(l))  # 一种差的效果
# [[1 1 1]
#  [1 1 1]
#  [1 1 1]]
l1 = np.arange(14, 2, -1).reshape((3, 4))
print(l1)
# [[14 13 12 11]
#  [10  9  8  7]
#  [ 6  5  4  3]]
print(np.sort(l1))  # 逐行进行排序，排序不改变源数据，看下面的转置矩阵是对源矩阵进行操作的
# [[11 12 13 14]
#  [ 7  8  9 10]
#  [ 3  4  5  6]]
print(np.transpose(l1))  # 实现对矩阵的转置
print(l1.T)
# [[14 10  6]
#  [13  9  5]
#  [12  8  4]
#  [11  7  3]]
print((l1.T).dot(l1))
print(np.clip(l1, 5, 9))  # l1中的元素。所有小于5的数都等于5，所有大于9的数都等于9
# [[9 9 9 9]
#  [9 9 8 7]
#  [6 5 5 5]]
