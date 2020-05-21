"""
@author:Liushihao
@time:2020/5/20:9:29
@email:Liushihao_1224@163.com
@describe:
编写一个程序实现如下功能：
(1)随机产生20个1～100之间的随机整数，写入文本文件sjs.txt中。
(2)从文本文件sjs.txt中读出数据，计算并输出标准方差。
"""
import random
import numpy as np
with open("file/sjs.txt","w") as fp:
    for i in range(0, 20):
        fp.write(str(random.randint(1, 100)))
        fp.write("\n")

sum = 0
arr = np.array([])
with open("file/sjs.txt","r") as fp:
    for line in fp:
        sum = sum + int(line)
        arr = np.append(arr, int(line))

print("随机生成的数组为：")
print(arr)
arr_std = np.std(arr,ddof=1)
print("随机生成的数组的标准差为：")
print(arr_std)