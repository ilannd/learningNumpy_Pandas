import numpy as np

a = np.arange(12).reshape((3, 4))
print(a)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]
print(np.split(a, 2, axis=1))  # 分割成两个array，对列进行操作  注意分割的个数，不能进行不等的分割，比如print(np.split(a, 3, axis=1))就会报错
# [array([[0, 1],
#        [4, 5],
#        [8, 9]]), array([[ 2,  3],
#        [ 6,  7],
#        [10, 11]])]
print(np.split(a, 3, axis=0))  # 分割成三个array，对行进行操作
# [array([[0, 1, 2, 3]]), array([[4, 5, 6, 7]]), array([[ 8,  9, 10, 11]])]

# 进行不等量的分割
print(np.array_split(a, 3, axis=1))
# [array([[0, 1],
#        [4, 5],
#        [8, 9]]), array([[ 2],
#        [ 6],
#        [10]]), array([[ 3],
#        [ 7],
#        [11]])]

print(np.vsplit(a, 3))  # 与print(np.split(a, 3, axis=0))等价
# [array([[0, 1, 2, 3]]), array([[4, 5, 6, 7]]), array([[ 8,  9, 10, 11]])]
print(np.hsplit(a, 2))  # 与print(np.split(a, 2, axis=1))等价
# [array([[0, 1],
#        [4, 5],
#        [8, 9]]), array([[ 2,  3],
#        [ 6,  7],
#        [10, 11]])]