#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from conf import config
from core import rw, manager, teacher, student


# 定义用户字典和功能字典
user_dic = rw.read(config.userinfo)
admin_actions = {'1': manager.Manager.create_teacher, '2': manager.Manager.create_student,
                 '3': manager.Manager.create_course, '4': manager.Manager.create_classes,
                 '5': manager.Manager.boundclass, '6': manager.Manager.show_teacher,
                 '7': manager.Manager.show_student, '8': manager.Manager.show_course, '9': manager.Manager.show_classes}
teacher_actions = {'1': teacher.Teacher.show, '2': teacher.Teacher.choice_classes, '3': teacher.Teacher.show_student}
student_actions = {'1': student.Student.show, '2': student.Student.choice_classes, '3': student.Student.pay}
print('用户参考：%s' % user_dic)


def login(func):
    def inner(*args, **kwargs):
        count = 0
        while count < 3:
            user_name = input("请输入用户名：").strip()
            user_pass = input("请输入密码：").strip()
            for user_item in user_dic.keys():
                if user_name == user_item and user_pass == user_dic[user_item][0]:
                    print("用户" + user_name + "登录成功！")
                    func(user_name, user_dic[user_item][1])
                    return
            else:
                print("用户名密码输入有误！")
            count += 1
        else:
            print("输入错误次数过多，稍后重试！")
            exit()
    return inner


@login
def main(name, who):
    # 打印欢迎信息login得到返回值打印对应功能菜单通过角色对象去调用
    if who == "admin":
        print('欢迎管理员登录,请选择操作！')
        while True:
            for key in manager.Manager.menu:
                print('%-6s-->> [%s]' % (key[0], key[1]))
            choice = input('请选择[]内的参数进行操作！(q退出）')
            if choice.isdigit():
                if choice in admin_actions.keys():
                    func = admin_actions[choice]
                    func(name)
            elif choice == 'q':
                exit('再见')
            else:
                print('参数输入错误！')
    elif who == "teacher":
        print('欢迎讲师%s登录,请选择操作！' % name)
        while True:
            for key in teacher.Teacher.menu:
                print('%-6s-->> [%s]' % (key[0], key[1]))
            choice = input('请选择[]内的参数进行操作！(q退出）')
            if choice.isdigit():
                if choice in teacher_actions.keys():
                    func = teacher_actions[choice]
                    func(name)
            elif choice == 'q':
                exit('再见')
            else:
                print("选择错误！")

    elif who == "student":
        print('欢迎学生%s登录,请选择操作！' % name)
        while True:
            for key in student.Student.menu:
                print('%-6s-->> [%s]' % (key[0], key[1]))
            choice = input('请选择[]内的参数进行操作！(q退出）')
            if choice.isdigit():
                if choice in student_actions.keys():
                    func = student_actions[choice]
                    func(name)
            elif choice == 'q':
                exit('再见')
            else:
                print("选择错误！")
    else:
        print("还未分配！")
