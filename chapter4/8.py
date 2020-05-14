"""
@author:Liushihao
@time:2020/3/27:10:08
@email:Liushihao_1224@163.com
@describe:
"""
items = ["breakfast", "lunch", "dinner", "others"]
breakfast = float(input("输入早餐费用:"))
lunch = float(input("输入中餐费用:"))
dinner = float(input("输入晚餐费用:"))
others = float(input("输入其他费用:"))
pay = [breakfast, lunch, dinner, others]
all_day = dict(zip(items, pay))
sum = sum(pay)
all_day["all_pay"] = sum
print(all_day)
print("费用的总和为：", all_day["all_pay"])