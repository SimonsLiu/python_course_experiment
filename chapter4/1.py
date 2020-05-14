"""
@author:Liushihao
@time:2020/3/26:19:28
@email:Liushihao_1224@163.com
@describe:
"""
a = [1,2,3,4]
b = [5,6,7,8]
# 第一种合并a,b的方法
a.extend(b)
print(a)
# 第二种合并a,b的方法
a = [1,2,3,4]
b = [5,6,7,8]
c = a+b
print(c)