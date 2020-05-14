"""
@author:Liushihao
@time:2020/3/5:11:58
@email:Liushihao_1224@163.com
@describe:
"""
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list1 = []
list2 = []
list3 = []
for e in list:
    if e % 2 != 0:
        list1.append(e)
    else:
        list2.append(e)

print("list1:", list1)
print("list2:", list2)

for i in range(len(list1)):
    num = list1[i] * 10 + list2[i]
    list3.append(num)

print("list3:", list3)
