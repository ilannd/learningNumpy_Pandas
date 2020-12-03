import pandas as pd

data = pd.read_csv('student.csv')
print(data)
# pandas 自动给加上了索引
#     Student ID   name  \tage gender
# 0         1100  kelly     22      f
# 1         1101    clo     21      f
# 2         1102  tilly     22      f
# 3         1103  tongy     24      m
# 4         1104  david     20      m
# 5         1105  catty     22      f
# 6         1106      m      3      f
# 7         1107      n     43      m
# 8         1108      a     13      m
# 9         1109      s     12      m
# 10        1110  david     33      m
# 11        1111     dw      3      f
# 12        1112      q     23      m
# 13        1113      w     21      f

data.to_pickle('student.pickle')