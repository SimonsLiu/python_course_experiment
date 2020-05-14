"""
@author:Liushihao
@time:2020/3/18:15:34
@email:Liushihao_1224@163.com
@describe:
"""
# 开始默认为平年
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
year, month = input("输入年份和月份(输入用空格隔开):").split(" ")
year = int(year)
month = int(month)
if year%400==0 or (year%4==0 and year%100!=0):
    month_days[2] = 29

print("%d年%d月有%d天"%(year, month,  month_days[month]))