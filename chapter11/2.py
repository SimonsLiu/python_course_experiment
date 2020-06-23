"""
@author:Liushihao
@time:2020/6/18:13:43
@email:Liushihao_1224@163.com
@describe:
编写一个“员工信息管理系统”实现对员工信息的管理，要求如下：
(1)员工信息存储在数据库中，数据库可以选择SQLite3、ACCESS、MySQL、MongoDB或其他数据库中的一种，但不能与第1题所选择的数据库相同。
(2)数据库中有3张表：员工信息表tb_emp、专业表tb_profession、部门表tb_dept。
(3)员工信息表tb_emp中包括字段：编号eid、姓名name、性别sex、出生日期birthday、个人介绍intro、专业profession和部门dept。
   专业表tb_profession中包括字段：编号id和名称name。
   部门表tb_dept中包括字段：编号id、名称name。
(4)专业表tb_profession的id和tb_dept中的id分别是员工信息表tb_emp中字段profession和dept的外键。
(5)程序运行后，可以从系统中查询、添加、修改和删除员工信息。
"""
# 第一题选择的mysql，本题选择sqlite3
import sqlite3
conn = sqlite3.connect('Employee_Information.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE tb_profession
                 (id int primary key not null,
                  name text not null
                  )''')
cursor.execute('''CREATE TABLE tb_dept
                (id int primary key not null,
                 name text not null
                )''')

# 初始化专业和部门信息
cursor.execute('''INSERT INTO tb_profession (id, name) VALUES (1, '计算机');''')
cursor.execute('''INSERT INTO tb_profession (id, name) VALUES (2, '安保');''')
cursor.execute('''INSERT INTO tb_profession (id, name) VALUES (3, '会计');''')
cursor.execute('''INSERT INTO tb_dept (id, name) VALUES (1, '技术部门');''')
cursor.execute('''INSERT INTO tb_dept (id, name) VALUES (2, '安全部门');''')
cursor.execute('''INSERT INTO tb_dept (id, name) VALUES (3, '财务部门');''')

# print("初始化1")
# 新建表格
try:
    cursor.execute('''CREATE TABLE tb_emp 
                     (eid int primary key not null,
                      name text not null,
                      sex text not null,
                      birthday date not null,
                      intro text not null,
                      profession int references tb_profession(id),
                      dept int references tb_dept(id)
                      )''')
    print('initialized successfully!!!')
except:
    print("initialized not successfully!!!")
    pass

def all_select():
    cursor.execute('SELECT * FROM tb_emp')
    all_data = cursor.fetchall()
    if (all_data == []):
        print('数据库表中无数据！')
    else:
        for line in all_data:
            for item in line:
                print(item, end=' ')
            print()

def eid_select():
    eid = int(input("请输入需要查询的员工编号："))
    sql = '''
           SELECT * FROM tb_emp WHERE eid = ?
           '''
    cursor.execute(sql, (eid,))
    eid_infor=cursor.fetchone()
    if (eid_infor == None):
        print('查无编号为%s的员工'%eid)
    else:
        # list_p_d = []
        sql_1 = '''
           SELECT name FROM tb_profession WHERE id = ?
           '''
        cursor.execute(sql_1, (eid_infor[5],))
        p = cursor.fetchone()[0]
        sql_2 = '''
                   SELECT name FROM tb_dept WHERE id = ?
                   '''
        cursor.execute(sql_2, (eid_infor[6],))
        d = cursor.fetchone()[0]
        print(p,d)
        print('编号为%s的员工信息如下：姓名：%s、性别：%s、出生日期：%s、个人介绍：%s、专业：%s、部门：%s'
              %(eid_infor[0],eid_infor[1],eid_infor[2],eid_infor[3],eid_infor[4],p,d))

def add():
    print('请输入员工编号、姓名、性别、生日、个人介绍、专业、部门(空格隔开)：')
    infor = input().strip(' ').split(' ')
    print(infor)
    add_sql = '''INSERT INTO tb_emp
                 (eid, name, sex, birthday, intro, profession, dept) 
                 VALUES (?,?,?,?,?,?,?);'''
    cursor.execute(add_sql, infor)
    conn.commit()
    print("添加员工信息成功！")

def delete():
    eid = int(input("请输入需要删除的员工的编号:"))
    delete = '''DELETE FROM tb_emp WHERE eid=?'''
    cursor.execute(delete, (eid,))
    conn.commit()
    print('删除员工数据成功')

def update():
    eid = int(input("请输入需要修改信息员工的编号："))
    # 个人介绍intro、专业profession和部门dept。
    intro= input("请输入修改的个人介绍：")
    profession = int(input("请输入修改的专业："))
    dept = int(input("请输入修改的部门："))
    update = '''UPDATE tb_emp SET intro=?,profession=?,dept=? WHERE eid=?'''
    cursor.execute(update, (intro, profession, dept, eid))
    conn.commit()
    print('更新员工数据成功')


print("===========================职员信息管理系统==============================")
while True:
    print('0--退出    1--添加    2--删除    3--修改    4--根据编号查询    5--查询所有')
    # 输入，接收用户输入的数字，执行相应的操作
    command = int(input("请输入你的操作："))
    if command == 0:
        # 退出系统
        print("退出系统成功!")
        conn.close()
        exit()
    elif command == 1:
        add()
    elif command == 2:
        delete()
    elif command == 3:
        update()
    elif command == 4:
        eid_select()
    elif command == 5:
        all_select()
    else:
        print("请输入正确的编号！")