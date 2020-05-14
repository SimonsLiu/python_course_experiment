"""
@author:Liushihao
@time:2020/4/27:16:33
@email:Liushihao_1224@163.com
@describe:
使用Random模块和NumPy库生成一个3行4列的多维数组，数组中的每个元素为1～100之间的随机整数，然后求该数组所有元素的平均值。
"""
import numpy as np
arr = np.random.randint(1,100, (3,4))
print("生成的随机数组：")
print(arr)
print("该数组所有元素的平均值%f"%(arr.sum()/(3*4)))