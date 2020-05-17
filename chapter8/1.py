"""
@author:Liushihao
@time:2020/5/16:15:17
@email:Liushihao_1224@163.com
@describe:编写一个程序，使用正则表达式校验输入的手机号是否正确。
"""
import re

phone_pat = re.compile('^(13\d|14[5-9]|15[0-35-9]|166|17[0-8]|18\d|19[8-9])\d{8}$')

while True:
    phone_number = input("请输入一个手机号：")
    result = re.search(phone_pat, phone_number)
    if result:
        print("手机号正常")
    else:
        print("手机号不正常")