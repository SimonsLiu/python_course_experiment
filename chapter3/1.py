"""
@author:Liushihao
@time:2020/3/18:0:27
@email:Liushihao_1224@163.com
@describe:
"""
a = input("输入a:")
b = input("输入b:")
c = input("输入c:")
print("从大到小顺序依次为：")
if a>b:
    if b>c:
        print("a,b,c")
    elif c>a:
        print("c,a,b")
    else:
        print("a,c,b")
else:
    if a>c:
        print("b, a, c")
    elif c>b:
        print("c,b,a")
    else:
        print("b,c,a")