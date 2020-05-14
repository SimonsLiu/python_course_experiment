"""
@author:Liushihao
@time:2020/3/5:10:24
@email:Liushihao_1224@163.com
@describe:
"""
import sympy as sp

x = sp.symbols("x")
f = x * x + 4 * x + 3
x = sp.solve(f)
print("x1 = %f, x2 = %f" % (x[0], x[1]))
