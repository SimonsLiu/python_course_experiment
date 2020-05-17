"""
@author:Liushihao
@time:2020/5/16:15:23
@email:Liushihao_1224@163.com
@describe: 编写一个程序，使用正则表达式校验输入的车牌号是否正确。
"""
import re
car_at = re.compile('^(([\u4e00-\u9fa5]{1}[A-Z]{1})[-]?|([wW][Jj][\u4e00-\u9fa5]{1}[-]?)|([a-zA-Z]{2}))[A-Za-z0-9]{5}$')
while True:
    car_num = input("请输入车牌号: ")
    result = re.search(car_at, car_num)
    if result:
        print("车牌号正确")
    else:
        print("车牌号不正确")