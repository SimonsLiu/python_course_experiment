"""
@author:Liushihao
@time:2020/5/20:21:48
@email:Liushihao_1224@163.com
@describe: 有两个文本文件(a.txt和b.txt)，各存放一行英文字母，要求把这两个文件中的信息合并(按字母顺序排列)，写到一个新文件c.txt中。
"""
str1 = open("file/a.txt","r").read()
str2 = open("file/b.txt","r").read()
str3 = str1 + str2
str_list = sorted(str3)
str4 = ''
for i in str_list:
    str4 = str4 + i
print(str4)
open("file/c.txt","w").write(str4)