import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# plot data

# Seires
data = pd.Series(np.random.randn(1000), index=np.arange(1000))  # 这里定义的index就是本来默认的index
data = data.cumsum()  # cumsum()是一个累加的一个效果

# DataFrame
data = pd.DataFrame(np.random.randn(1000, 4), index=np.arange(1000), columns=list("ABCD"))
# 1000个数据点，4个数据的属性，实际上有4000个数据了。四个属性就是后面的ABCD
data = data.cumsum()

print(data.head())  # 默认输出前五个数据    data.head(3)就是输出前三个数据
#           A         B         C         D
# 0  0.984738 -0.195490  0.860576  0.474114
# 1 -0.312942 -0.427268  0.591883 -0.608748
# 2 -0.408836  0.273114  0.192434 -0.936533
# 3 -1.108617  0.950784  1.105596 -1.714503
# 4  0.158985 -0.014241  0.446807 -2.022935
# data.plot()
# plot methods:
# 'bar','hist','box','kde','area','scatter','hexbin','pie'
ax = data.plot.scatter(x='A', y='B', color='DarkBlue', label='Class1')
data.plot.scatter(x='A', y='C', color='DarkGreen', label='Class2',ax=ax)
plt.show()
