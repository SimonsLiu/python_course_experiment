"""
@author:Liushihao
@time:2020/4/8:21:55
@email:Liushihao_1224@163.com
@describe:
"""
def fbnq(i):
    if i==1 or i==2:
        return 1
    else:
        return fbnq(i-1)+fbnq(i-2)

def fbnq_sum(i):
    if i==1:
        return 1
    else:
        return fbnq_sum(i-1)+fbnq(i)

i = int(input("请输入一个整数i,将返回斐波那契数列第i项:"))
print("斐波那契数列第%d项为%d"%(i, fbnq(i)))
n = int(input("请输入一个整数n,将返回斐波那契数列前n项的和:"))
print("斐波那契数列前%d项的和为%d"%(n, fbnq_sum(n)))