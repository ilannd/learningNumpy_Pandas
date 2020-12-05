import numpy as np

a = np.array([1, 1, 1])
b = np.array([2, 2, 2])

# 上下合并
c = np.vstack((a, b))
print(c)  # vertical stack
# [[1 1 1]
#  [2 2 2]]
print(a.shape)  # (3,)
print(c.shape)  # (2, 3)

# 左右合并
d = np.hstack((a, b))  # horizontal stack
print(d)  # [1 1 1 2 2 2]
print(d.shape)  # (6,)

# 将列表变成一个矩阵
print(a.T)  # [1 1 1]  # 我们不能用transpose把一个序列变成一个矩阵
print(a.T.shape)  # (3,)

print(a[np.newaxis, :])  # [[1 1 1]] # 在行上加了一个维度
print(a[np.newaxis, :].shape)  # (1, 3)

print(a[:, np.newaxis])  # [[1 1 1]] # 在列上加了一个维度
# [[1]
#  [1]
#  [1]]
print(a[:, np.newaxis].shape)  # (3, 1)

# 对多个array进行纵向和横向的合并
a1 = a[np.newaxis, :]  # a1 变为[[1, 1, 1]]
b1 = b[np.newaxis, :]   # b1 变为[[2, 2, 2]]
e = np.concatenate((a1, b1, b1, a1), axis=0)
print(e)
# [[1 1 1]
#  [2 2 2]
#  [2 2 2]
#  [1 1 1]]

f = np.concatenate((a1, b1, b1, a1), axis=1)
# [[1 1 1 2 2 2 2 2 2 1 1 1]]
# 使用np.concatenate((a,b),axis=1)会报错
# 这是因为a和b都是一维数据，只有一个维度，也就是axis=0，不存在axis=1
# np.vstack((A,B))可以实现上下合并，但只能两个向量合并
print(f)
