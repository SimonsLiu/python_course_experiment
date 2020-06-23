"""
@author:Liushihao
@time:2020/6/17:11:34
@email:Liushihao_1224@163.com
@describe:
1．编写一个“学生成绩管理系统”实现对学生成绩的管理，要求如下：
(1)成绩信息存储在数据库中，数据库选择SQLite3、ACCESS、MySQL、MongoDB或其他数据库之中的一种。
(2)数据库中只有一张数据表即学生成绩表tb_grade，该表至少包括下列字段：学号sno、姓名sname、性别sex、出生日期birthday、高等数学maths、英语english和操作系统os。
(3)程序运行后，可以动态地从系统中查询、添加、修改和删除学生成绩。
"""
import pymysql
# 连接一个数据库
db = pymysql.connect(host='localhost', user='root', password='123456', database='studentgrade')
# 创建一个游标
cursor = db.cursor()
# 新建一个表格
try:
    cursor.execute(
        '''CREATE TABLE tb_stu_grade 
        (sno varchar(12) primary key not null,
         sname varchar(4) not null,
         sex varchar(4) not null,
         birthday varchar(12) not null,
         maths varchar(12),
         english varchar(12),
         os varchar(12))''')
    print('新建表格成功！')
except:
    pass

def select():
    cursor.execute('SELECT * FROM tb_stu_grade')
    l = cursor.fetchall()
    if (l == ()):
        print('数据库内无数据！')
    else:
        for line in l:
            for item in line:
                print(item, end=' ')
            print()

def insert(sno, sname, sex, birthday, maths, english, os):
    insert_sql = '''INSERT INTO tb_stu_grade(sno, sname, sex, birthday, maths, english, os) VALUES (%s,%s,%s,%s,%s,%s,%s);'''
    insert_string = (sno, sname, sex, birthday, maths, english, os)
    cursor.execute(insert_sql, insert_string)
    db.commit()
    print('插入数据成功')

def update(sno, maths, english, os):
    update = '''UPDATE tb_stu_grade SET maths=%s,english=%s,os=%s WHERE sno=%s'''
    cursor.execute(update, (maths, english, os, sno))
    db.commit()
    print('更新数据成功')

def delete(sno):
    delete = '''DELETE FROM tb_stu_grade WHERE sno=%s'''
    cursor.execute(delete, (sno,))
    db.commit()
    print('删除数据成功')

def management():
    print('------------------学生成绩管理系统------------------')
    print('------------------操作命令编号如下------------------')
    print('-1--退出    0--查询    1--添加    2--修改    3--删除')
    print('---------------------------------------------------')
    while (True):
        i = input('请输入操作编号:')
        if (i == '-1'):
            db.close()
            print('关闭数据库连接')
            exit()
        elif (i == '0'):
            select()
        elif (i == '1'):
            print('请输入学号、姓名、性别、生日、数学成绩、英语成绩、操作系统成绩(空格隔开)：')
            j = input().strip(' ').split(' ')
            if (len(j) != 7):
                print('输入信息有误！输入信息个数错误！')
                continue
            else:
                try:
                    insert(j[0], j[1], j[2], j[3], j[4], j[5], j[6])
                except:
                    print('插入失败')
                    continue
        elif (i == '2'):
            print('请输入学号、数学成绩、英语成绩、操作系统成绩(空格隔开)：')
            j = input().strip(' ').split(' ')
            if (len(j) != 4):
                print('输入信息有误！输入信息个数错误！')
                continue
            else:
                update(j[0], j[1], j[2], j[3])
        elif (i == '3'):
            print('请输入目标学号：')
            j = input().strip(' ').split(' ')
            if (len(j) == 1):
                delete(j[0])
            else:
                print('输入信息有误！输入信息个数错误！')
                continue

if __name__ == '__main__':
    management()