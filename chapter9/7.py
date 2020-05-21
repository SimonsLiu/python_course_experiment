"""
@author:Liushihao
@time:2020/5/20:22:25
@email:Liushihao_1224@163.com
@describe:
编写一个程序，分别将一个数字、字符串、列表、元组、字典和集合写入一个二进制文件bFile.dat中，
然后从二进制文件bFile.dat中读出并显示。
"""
import pickle
num = 1
str1 = 'abc'
list1 = [1, 2, 3]
tuple1 = ('c', 'd', 'e')
dict1 = {"a":1, "b":2, "c":3}
set1 = {1, 3, 5, 7, 9}
data = [num, str1, list1, tuple1, dict1, set1]
with open("file/bFile.dat", "wb") as w_f:
    for i in data:
        pickle.dump(i, w_f)
    print("写入数据成功！！！")

with open("file/bFile.dat", "rb") as w_f:
    for i in range(0, len(data)):
        data0 = pickle.load(w_f)
        print("data%d:"%i)
        print(data0)
    print("读取数据成功")