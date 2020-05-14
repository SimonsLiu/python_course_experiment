"""
@author:Liushihao
@time:2020/3/27:10:08
@email:Liushihao_1224@163.com
@describe:
"""
stu_id = ["000", "001", "002", "003", "004"]
stu_score = [88, 99, 77, 89, 91]
grade = dict(zip(stu_id, stu_score))
print("初始化grade字典：",grade)
# 添加学生成绩
grade["005"] = 94
print("添加学号为005的成绩94之后：",grade)
# 修改字典中指定学生成绩
grade["004"] = 90
print("将学号为004的成绩修改为90之后：",grade)
# 删除指定学生成绩
grade.pop("001")
print("将学号为001的成绩删除后：",grade)
# 查询指定学生成绩
print("查询学号为003学生的成绩：", grade["003"])

max = max(grade.values())
min = min(grade.values())
ava = sum(grade.values())/len(grade)
print("最高分为：",max)
print("最低分为：",min)
print("平均分为：", ava)
