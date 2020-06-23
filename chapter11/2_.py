"""
@author:Liushihao
@time:2020/6/19:20:13
@email:Liushihao_1224@163.com
@describe:
"""
import sqlite3
conn = sqlite3.connect('Employee_Information.db')
cursor = conn.cursor()
try:
    cursor.execute('''CREATE TABLE tb_profession 
                 (id int primary key not null,
                  name text not null
                  )''')
    cursor.execute('''CREATE TABLE tb_dept 
                (id int primary key not null,
                 name text not null
                )''')
    cursor.execute('''CREATE TABLE tb_emp 
                     (eid int primary key not null,
                      name text not null,
                      sex text not null,
                      birthday date not null,
                      intro text not null,
                      foreign key(profession) references tb_profession(id),
                      foreign key(dept) references tb_dept(id),
                      )''')
    print('initialized successfully!!!')
except:
    print("initialized not successfully!!!")
    pass

def select():
    cursor.execute('SELECT * FROM tb_stu_grade')
    l=cursor.fetchall()
    if (l == []):
        print('无数据')
    else:
        for line in l:
            for item in line:
                print(item, end=' ')
            print()

def insert(conn, sno, sname, sex,birthday,maths,english,os):
    insert='''INSERT INTO tb_stu_grade VALUES (?,?,?,?,?,?,?);'''
    conn.execute(insert, (sno,sname,sex,birthday,maths,english,os))
    conn.commit()
    print('插入数据成功')

def update(conn,sno,maths,english,os):
    update='''UPDATE tb_stu_grade SET maths=?,english=?,os=? WHERE sno=?'''
    conn.execute(update, (maths,english,os,sno))
    conn.commit()
    print('更新数据成功')

def delete(conn, sno):
    delete = '''DELETE FROM tb_stu_grade WHERE sno=?'''
    conn.execute(delete,(sno,))
    conn.commit()
    print('删除数据成功')

def dict(self):
    info_dic = {}
    while True:
        name = input("请输入姓名：")
        info_dic["姓名"] = name
        age = input("请输入年龄：")
        info_dic["年龄"] = age
        student_num = input("请输入学号：")
        info_dic["学号"] = student_num
        qq = input("请输入QQ号码:")
        info_dic["QQ"] = qq
        weiXin = input("请输入微信号：")
        info_dic["微信"] = weiXin
        address = input("请输入地址：")
        info_dic["地址"] = address
        print(info_dic)
        for k, v in info_dic.items():
            print("%s : %s" % (k, v))
info_list = []

while True:
    # 界面
    print("========职员信息管理系统========")
    print("-----1、添加员工信息-----")
    print("-----2、删除员工信息-----")
    print("-----3、修改员工信息-----")
    print("-----4、查询员工信息-----")
    print("-----0、退出系统-----")
    print("-" * 30)

    # 输入，接收用户输入的数字，执行相应的操作
    command = int(input("请输入你的操作："))

    # 通过判断用户输入的数字是1，还是2，还是3...执行相应操作
    if command == 1:
        # 添加员工信息
        name = input("请输入员工姓名：")
        worker_id = input("请输入员工id：")
        if (len(worker_id) == 5) and (worker_id.isdigit()):
            card_id = input("请输入身份证号：")
            if len(card_id) == 18 and (card_id.isdigit() or (card_id[0:17].isdigit() and card_id[-1] in "xX")):
                info_list.append({"姓名": name, "id": worker_id, "身份证": card_id})
                print("【info】:添加成功")
                print(info_list)
            else:
                print("【ERROR】：身份证必须是18位，除了第18位可以为x，其余只能是数字")
        else:
            print("【ERROR】：员工id必须是五位数字组成")

    elif command == 2:
        # 删除员工信息
        print(info_list)
        name = input("删除：请输入姓名：")
        for i in info_list:
            if name in i.values():
                del info_list[info_list.index(i)]
                print("【info】：删除成功")
                print(info_list)
                break
        else:
            print("【Error】：查无此人")
    elif command == 3:
        # 修改员工信息
        name = input("修改：请输入姓名：")
        for i in info_list:
            if name in i.values():
                worker_id = input("请输入修改后的员工id：")
                if (len(worker_id) == 5) and (worker_id.isdigit()):
                    card_id = input("请输入修改后的身份证号：")
                    if len(card_id) == 18 and (card_id.isdigit() or (card_id[0:17].isdigit() and card_id[-1] in "xX")):
                        info_list[info_list.index(i)] = {"姓名": name, "id": worker_id, "身份证": card_id}
                        print(info_list)
                        print("info：修改成功")
                        break
                    else:
                        print("ERROR：身份证必须是18位，除了第18位可以为x，其余只能是数字")
                else:
                    print("ERROR：员工id必须是五位数字组成")
        else:
            print("Error：查无此人")


    elif command == 4:
        # 查询学生信息
        userName = "admin"
        passWord = "123456"
        userName_input = input("请输入你的用户名：")
        passWord_input = input("请输入你的密码：")
        if (userName == userName_input) and (passWord == passWord_input):
            name = input("查询：请输入姓名：")
            for i in info_list:
                if name in i.values():
                    for k, v in i.items():
                        print("%s : %s" % (k, v))
                    break
            else:
                print("Error：查无此人")
        else:
            print("Error：用户名或密码错误")
    elif command == 5:
        # 查询所有学生信息
        userName = "admin"
        passWord = "123456"
        userName_input = input("请输入你的用户名：")
        passWord_input = input("请输入你的密码：")
        if (userName == userName_input) and (passWord == passWord_input):
            for i in info_list:
                for k, v in i.items():
                    print("%s : %s" % (k, v))
                    print("----------------")
        else:
            print("Error：用户名或密码错误")


    elif command == 6:
        # 退出系统
        print("退出系统成功，谢谢使用")
        break
    else:
        print("Error:请输入1-6之间的整数")