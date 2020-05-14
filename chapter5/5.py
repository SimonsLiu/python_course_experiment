"""
@author:Liushihao
@time:2020/4/8:21:55
@email:Liushihao_1224@163.com
@describe:
"""
def func(n):
    if n%2 ==0:
        sum = 0
        i=1
        while(i<=n):
            sum+=1/(2*i)
            i+=1
        return sum
    else:
        sum = 0
        i = 0
        while (i <= n):
            sum += 1 / (2 * i+1)
            i += 1
        return sum

print(func(2))
print(func(1))