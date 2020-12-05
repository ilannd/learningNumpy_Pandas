import numpy as np

a = np.arange(4)
print(a)
b = a
c = a
d = b
a[0] = 11
print(a)
print(b is a)  # b 就是 a,修改a 就是修改b
print(b)
print(c is a)
print(c)
print(d is a)
print(d)
d[1:3] = [22, 33]
print(d)
print(a, b, c)

e = a.copy()  # deep copy
print(e)  # [11 22 33  3]
a[3] = 44
print(a, e)  # [11 22 33 44] [11 22 33  3]  改a 中的数，对e 没有影响


f = [1, 2, 3]
g = f[:]  # 感觉这就是相当于深拷贝
print(f, g)
#  [1, 2, 3] [1, 2, 3]
f[1] = 22
print(f, g)
# [1, 22, 3] [1, 2, 3]
