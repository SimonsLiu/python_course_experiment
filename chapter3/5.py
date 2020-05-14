"""
@author:Liushihao
@time:2020/3/18:15:34
@email:Liushihao_1224@163.com
@describe:
"""
list = [1,2,3,4]
count = 0
for i in list:
    for j in list:
        for k in list:
            a = i*100+j*10+k
            print(a)
            count+=1

print("一共能够组成", count, "个互不相同三位数")