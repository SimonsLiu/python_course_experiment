"""
@author:Liushihao
@time:2020/3/26:19:28
@email:Liushihao_1224@163.com
@describe:
"""
import random
arry = [i for i in range(1,101)]
list = random.sample(arry, 10)
print("变化前",list)
for i in range(0,len(list)):
    if list[i]%2==0:
        list[i] = pow(list[i], 3)
    else:
        list[i] = pow(list[i], 2)

print("变化后",list)