"""
@author:Liushihao
@time:2020/4/8:21:55
@email:Liushihao_1224@163.com
@describe:
"""
def func(str1, str2):
    if str2 in str1:
        str3 = str1.replace(str2, "")
        return str3

    else:
        print("在str1中不存在str2，无法从str1中删除str2")

str1, str2 = input("请输入两个字符串，并用“,”隔开:").split(",")

print("将字符串str1中出现的字符串str2删除结果:",func(str1, str2))