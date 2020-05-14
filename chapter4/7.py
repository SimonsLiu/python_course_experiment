"""
@author:Liushihao
@time:2020/3/27:10:08
@email:Liushihao_1224@163.com
@describe:
"""
set1 = {2, 5, 9, 1, 3}
set2 = {3, 6, 8, 2, 5}
set1.add(7)
print("向set1中添加一个新的元素7后：",set1)
set_a = set1 | set2
set_b = set1 & set2
set_c = set1 - set2
print("set1和set2的并集：", set_a)
print("set1和set2的交集：", set_b)
print("set1和set2的差集：", set_c)

