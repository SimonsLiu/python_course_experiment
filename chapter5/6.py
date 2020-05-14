"""
@author:Liushihao
@time:2020/4/8:21:55
@email:Liushihao_1224@163.com
@describe:
"""
def Recursive(n):
    if n==1:
        return 10
    else:
        return Recursive(n-1)+2

def no_Recursive(n):
    age = 10
    i=1
    while(i<n):
        age+=2
        i+=1
    return age

print("采用递归方法，第五个人的年龄为：",Recursive(5))
print("采用非递归方法，第五个人的年龄为：",no_Recursive(5))