"""
@author:Liushihao
@time:2020/3/5:10:46
@email:Liushihao_1224@163.com
@describe:
"""
import numpy as np
num = int(input("请输入一个四位整数:"))
a = int(num / 1000)
b = int(num / 100 % 10)
c = int(num / 10) % 10
d = num % 10
list_ = np.array([a, b, c, d])
list_ = (list_ + 5)%10
list_[0],list_[3] = list_[3],list_[0]
list_[1],list_[2] = list_[2],list_[1]
str = "".join(str(i) for i in list_)
print("4位整数数据%d加密为：%s"%(num,str))
