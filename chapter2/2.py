"""
@author:Liushihao
@time:2020/3/5:9:50
@email:Liushihao_1224@163.com
@describe:
"""
import math
def fuction(x, y, z):
    f = (3*x + 4*math.sqrt(x*x+2*y*y)) / (1 + math.cos(math.pow(z, 3)))
    return f

print("result=",fuction(1, 2, 0))