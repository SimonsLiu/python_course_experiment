"""
@author:Liushihao
@time:2020/3/27:10:08
@email:Liushihao_1224@163.com
@describe:
"""
grade = (68, 87, 83, 91, 93, 79, 68, 86, 66, 78)
print("grade中的第2个元素为：", grade[1])
print("grade中的第3~7个元素为：", grade[2:7])
print("grade中是否包含成绩87：", (87 in grade))
print("grade中成绩为78的学生学号为：", grade.index(78))
print("grade中成绩68出现的次数为：", grade.count(68))
print("grade中元素的个数为：", len(grade))