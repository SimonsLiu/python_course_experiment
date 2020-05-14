"""
@author:Liushihao
@time:2020/3/18:15:34
@email:Liushihao_1224@163.com
@describe:
"""
a = int(input("输入一个不多于5位的正整数："))
a_str = str(a)
print("该正整数的位数为：",a_str.__len__())
for i in a_str[::-1]:
    print(i)


