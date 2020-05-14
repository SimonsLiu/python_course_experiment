"""
@author:Liushihao
@time:2020/4/8:21:55
@email:Liushihao_1224@163.com
@describe:
"""
from math import sqrt
# 判断n是否为素数
def isprime(n):
    i = 2
    while i<=int(sqrt(n)):
        if n%i==0:
            return False
        i+=1
    return True

# 输入n将返回2~n之间的所有素数,格式为列表
def isprimelist(n):
    list_prime = []
    i = 2
    for m in range(i,n+1):
        if isprime(m):
            list_prime.append(m)
    return list_prime

def isGDBH(n):
    ans = []
    list_prime = isprimelist(100)
    for i in list_prime:
        a = n-i
        if a in list_prime:
            str1 = str(n)+"="+str(i)+"+"+str(a)
            list_prime.remove(a)
            ans.append(str1)
    return ans


n = int(input("请输入6～100之间的偶数："))
print(isGDBH(n))