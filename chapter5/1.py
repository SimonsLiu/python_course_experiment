"""
@author:Liushihao
@time:2020/4/8:21:55
@email:Liushihao_1224@163.com
@describe:
"""
def func(n):
    return '{0:b}'.format(n)

n = int(input("请输入一个整数，转化为二进制数:"))
print("%d转化为二进制数为：%s"%(n, func(n)))