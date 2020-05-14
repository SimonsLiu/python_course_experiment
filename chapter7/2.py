"""
@author:Liushihao
@time:2020/4/27:16:33
@email:Liushihao_1224@163.com
@describe:
"""
from datetime import datetime
import time

dt = datetime.now()
print("当前年份: %d,当前月份: %d,当前日期: %d"%(dt.year,dt.month,dt.day))
print("本周是今年的第",time.strftime("%W"),"周")  # 索引从0开始
today_weekday = datetime.now().isoweekday()
print("今天是该周的第%d天"%today_weekday)