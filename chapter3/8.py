"""
@author:Liushihao
@time:2020/3/18:15:34
@email:Liushihao_1224@163.com
@describe:
"""
n = int(input("输入图形的层数："))
s = '* '
for i in range(1, n+1, 2):
    print((s * i).center(14))
for i in reversed(range(1, n-1, 2)):
    print((s * i).center(14))

# n = 7
#
# for i in range(-4, 5):
#     if i<0:
#         j = -i
#     else:
#         j = i
#     print(' '*j + '*'*(n-2*j))