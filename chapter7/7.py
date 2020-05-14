"""
@author:Liushihao
@time:2020/4/27:16:33
@email:Liushihao_1224@163.com
@describe:使用Matplotlib库绘制 y = 2x+1 和 y=x^2 的图形，并设置坐标轴的名称和图例。
"""
import numpy as np
from matplotlib import pyplot as plt
x = np.arange(-5, 5.01, 0.01)
y1 = 2 * x + 1
y2 = x*x

fig, ax = plt.subplots()
line1, = ax.plot(x,y1)
line2, = ax.plot(x, y2)
ax.legend((line1, line2), ("y1=2x+1", "y2=x^2"))
plt.xlabel("x")
plt.ylabel("y")
plt.title("y=2x+1 and y=x^2")
plt.show()
