"""
@author:Liushihao
@time:2020/4/8:21:55
@email:Liushihao_1224@163.com
@describe:
"""
from math import pi
# Triangle, rectangle and circle
def deco(f):
    def wrapper(*args, **kwargs):
        if len(args)!=f.__code__.co_argcount:
            if type(args[0])!=type(1):
                print("参数个数不正确且参数类型不符合")
            else:
                print("参数个数不正确")
            # return f(*args, **kwargs)
        else:
            if type(args[0])!=type(1):
                print("参数个数正确但参数类型不符合")
            elif type(args[0])==type(1):
                print("参数个数正确且参数类型符合")
                return f(*args, *kwargs)
            else:
                print("参数类型不符合")

    return wrapper

@deco
def Triangle(a, b, c):
    return a+b+c

@deco
def Rectangle(a,b):
    return 2*(a+b)

@deco
def Circle(r):
    return 2*pi*r

print(Circle(1))
print(Circle(1,1))
print(Circle("1",1))
print(Circle("1"))