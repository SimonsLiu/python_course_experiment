"""
@author:Liushihao
@time:2020/5/20:17:25
@email:Liushihao_1224@163.com
@describe: 编写一个程序，将文本文件file1.txt中的内容连接到文本文件file2.txt的内容后面。
"""
with open("file/file1.txt","r",encoding='UTF-8') as fp1:
    str = fp1.read()
    with open("file/file2.txt", "r+", encoding='UTF-8') as fp2:
        fp2.readlines()
        fp2.write(str)
    fp2.close()
fp1.close()