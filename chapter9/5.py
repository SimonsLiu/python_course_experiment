"""
@author:Liushihao
@time:2020/5/20:17:52
@email:Liushihao_1224@163.com
@describe:
创建一个名为grade.csv的文件，通过input()函数向文件中写入学生相关信息，
格式为“姓名，性别，年龄，语文成绩，数学成绩，英语成绩”，
当输入“-1”时结束输入。统计所有学生的总成绩、排序，并写入新文件statistics.csv中。
"""
import csv
import operator
# 建一个学生类 便于排序
class student:
    def __init__(self, name, sex, age, chinese, math, english):
        self.name  = name
        self.sex = sex
        self.age = age
        self.chinese = chinese
        self.math = math
        self.english = english
        self.sum = self.chinese+self.math+self.english
headers1 = ['姓名','性别','年龄','语文成绩','数学成绩','英语成绩']
print("请输入学生'姓名','性别','年龄','语文成绩','数学成绩','英语成绩'(-1结束)：")
with open('file/grade.csv', 'w', newline='',encoding='UTF-8') as file1:
    fw1 = csv.writer(file1)
    fw1.writerow(headers1)
    while True:
        data = input()
        if data == '-1':
            break
        else:
            data_list = data.split(',')
            fw1.writerow(data_list)
Student = []
with open('file/grade.csv', 'r+', newline='',encoding='UTF-8') as file1:
    fw1 = csv.reader(file1)
    rows = [row for row in fw1][1:]
    # 将grade.csv中的数据读取，然后存储于类对象中，然后将类对象用列表存储
    for stu in rows:
        Student.append(student(stu[0],stu[1],int(stu[2]),int(stu[3]), int(stu[4]), int(stu[5])))

# 排序时用于比较的指标
cmpfun = operator.attrgetter('sum')
# 从大到小排序，按照属性sum
Student.sort(key=cmpfun, reverse=True)
headers2 = ['姓名','性别','年龄','语文成绩','数学成绩','英语成绩','总成绩']
# 写入statistics.csv文件
with open('file/statistics.csv', 'w', newline='',encoding='UTF-8') as file2:
    fw2 = csv.writer(file2)
    fw2.writerow(headers2)
    data_stu = []
    for stu in Student:
        data_stu.append((stu.name, stu.sex, stu.age, stu.chinese, stu.math, stu.english, stu.sum))
    fw2.writerows(data_stu)