"""
@author:Liushihao
@time:2020/5/20:9:12
@email:Liushihao_1224@163.com
@describe: 编写一个程序，通过键盘将曹操的《观沧海》写入文本文件gch.txt中。
"""
with open("file/1.txt","w") as fp:
    gch = input("请输入《观沧海》：")
    num = fp.write(gch)
    print("观沧海一共有 %d 个字符（算上标点符号）！" % (num))
