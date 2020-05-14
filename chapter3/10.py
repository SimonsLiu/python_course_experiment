"""
@author:Liushihao
@time:2020/3/18:15:35
@email:Liushihao_1224@163.com
@describe:
"""

a_b = 100000 # 每天陌生人给富翁的钱
sum_a_b = 0  # 陌生人给富翁的钱的总数
b_a = 0.01   # 富翁给陌生人的第一天的钱
sum_b_a = 0  # 富翁给陌生人的钱的总数
n=1
while(n<=30):
    sum_a_b+=a_b
    sum_b_a+=b_a
    b_a*=2
    n+=1
print("陌生人给富翁一共%.2f元"%sum_a_b)
print("富翁给陌生人一共%.2f元"%sum_b_a)
