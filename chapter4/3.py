"""
@author:Liushihao
@time:2020/3/26:19:28
@email:Liushihao_1224@163.com
@describe:
"""
list = [3, 8, 11, 26, 47]
a = int(input("输入一个新元素:"))
insert_index = 0
for i in range(0, len(list)):
    if a>list[i]:
        insert_index+=1
    else:
        break

list.insert(insert_index, a)
print(list)