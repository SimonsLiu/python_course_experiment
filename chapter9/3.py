"""
@author:Liushihao
@time:2020/5/20:17:12
@email:Liushihao_1224@163.com
@describe: 编写一个程序，将文本文件file1.txt中的内容复制到文本文件file2.txt(空文件)中。
"""
with open("file/file1.txt","r",encoding='UTF-8') as fp1:
    str = fp1.read()
    with open("file/file2.txt", "w", encoding='UTF-8') as fp2:
        fp2.write(str)
    fp2.close()
fp1.close()