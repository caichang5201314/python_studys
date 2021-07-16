"""
@File: demo.py
@Description: 描述
@Author: 蔡昶
@Email：caichangfast@qq.com
@Time:2021/6/23 - 8:56
"""


def menu():
    print("-" * 25)
    print("1、添加学生信息")
    print("2、删除学生信息")
    print("3、修改学生信息")
    print("4、查询学生信息")
    print("5、查看所有学生信息")
    print("6、退出系统")
    print("-" * 25)


stu = []


def is_id_exit(stu_id, stu_list=stu):
    for temp in stu_list:
        if temp["id"] == stu_id:
            return True
    return False


print("-" * 25)
print("欢迎使用学生信息管理系统 V1.0")

while True:
    menu()
    menu_id = int(input("请选择您使用的功能序列号："))

    if menu_id == 1:
        print("您选择了添加学生选项")
        name = input("请输入学生姓名：")
        age = input("请输入学生年龄：")
        while True:
            stu_id = input("请输入学生学号：")
            if (not is_id_exit(stu_id)):
                break
            print("学生ID已存在！")

        stu_info = {}
        stu_info["name"] = name
        stu_info["age"] = age
        stu_info["id"] = stu_id

        stu.append(stu_info)
        print("学生信息添加成功！")
    elif menu_id == 2:
        print("您选择了删除学生选项")
        stu_id = input("请输入要删除的学号：")
        if (is_id_exit(stu_id)):
            cnt = 0
        for temp in stu:
            if temp["id"] == stu_id:
                break;
            cnt = cnt + 1
            del stu[cnt]
            print("删除学生成功")
        else:
            print("您输入的学号不存在！")
    elif menu_id == 3:
        print("您选择了修改学生信息选项")
        input("请输入要修改的学号：")
        if (is_id_exit(stu_id)):
            stu_info["name"] = input("请输入要修改的名字：")
            stu_info["age"] = input("请输入要修改的年龄：")
            print(stu)
            print("修改成功")
        else:
            print("该ID不存在！")
    elif menu_id == 4:
        print("您选择了查询学生信息选项")
        stu_id = input("请输入要查询的学生学号：")
        if (is_id_exit(stu_id)):
            print("学生ID已存在！")
            print(stu)
        else:
            print("该ID不存在！")
    elif menu_id == 5:
        print("您选择了查询所有学生信息")
        print(stu)
    elif menu_id == 6:
        print("您选择了退出系统")
        break
