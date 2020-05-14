"""
@author:Liushihao
@time:2020/4/8:21:55
@email:Liushihao_1224@163.com
@describe:
"""
# 判断是否为“完数”
def isWs(n):
    list1 = []
    i = 1
    while(i<n):
        if n%i==0:
            list1.append(i)
        i+=1
    sum1 = sum(list1)
    if sum1==n:
        return True
    else:
        return False

n = int(input("请输入一个数，来判断是否为完数:"))
print(isWs(n))