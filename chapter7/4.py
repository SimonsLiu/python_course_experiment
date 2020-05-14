"""
@author:Liushihao
@time:2020/4/27:16:33
@email:Liushihao_1224@163.com
@describe:编写一个计算的函数，使用Timeit模块计算该函数的执行时间。
"""
import timeit
def cal():
    return sum(range(10001))

t = timeit.timeit(stmt="cal()", setup="from  __main__ import cal", number=10000)
print("计算10000次时间：%fs"%t)
print("计算一次时间：%fs"%(t/10000))