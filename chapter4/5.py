"""
@author:Liushihao
@time:2020/3/27:10:08
@email:Liushihao_1224@163.com
@describe:
"""
import random
import numpy as np
arry = [random.randint(1,10) for i in range(0,20)]
tuple1 = tuple(arry)
print("生成的随机元组为:", tuple1)
fre = np.zeros((10),np.int32)
for i in tuple1:
    fre[i-1]+=1

for i in range(1,11):
    print("%d出现的次数为:%d"%(i, fre[i-1]))