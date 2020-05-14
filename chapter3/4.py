"""
@author:Liushihao
@time:2020/3/18:15:34
@email:Liushihao_1224@163.com
@describe:
"""
def IsPrimeNumbers(a): # 判断素数函数
    for i in range(2, a):
        if a%i==0:
            flag = False
            return flag
    flag = True
    return flag

count = 0
for i in range(100, 1001):
    if(IsPrimeNumbers(i)):
        print(i)
        count+=1

print("100～1000之间的所有素数有：", count, "个")