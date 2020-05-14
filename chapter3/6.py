"""
@author:Liushihao
@time:2020/3/18:15:34
@email:Liushihao_1224@163.com
@describe:
"""
count = 0
for i in range(100,1000):
    a = i%10
    b = i//10%10
    c = i//100
    if a**3+b**3+c**3==i:
        print(i)
        count+=1

print("水仙花数一共有：%d个"%count )