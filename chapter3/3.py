"""
@author:Liushihao
@time:2020/3/18:15:34
@email:Liushihao_1224@163.com
@describe:
"""
sum = 0
for i in range(1,101):
    if i%4==0:
        sum+=i

print("1～100范围内能被4整除的所有数的和为：",sum)