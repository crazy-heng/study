#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 管理员类
import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from conf import config
from core import rw, teacher, student


class Manager:
    menu = [['创建讲师', '1'], ['创建学生', '2'], ['创建课程', '3'], ['创建班级', '4'], ['创建绑定', '5'],
            ['查看讲师', '6'], ['查看学生', '7'], ['查看课程', '8'], ['查看班级', '9']]

    def __init__(self, name):
        self.name = name

    def create_teacher(self):
        # 输入老师用户名密码存入登陆信息到db
        print('---创建讲师---')
        name = input("输入讲师姓名：").strip()
        password = input("输入讲师密码：").strip()
        config.user_dic[name] = [password, 'teacher']
        rw.write(config.userinfo, config.user_dic)
        # 输入老师所在学校 用户名 身份 学校
        t = teacher.Teacher(name)
        rw.write("%s%s" % (config.teacher, name), t.__dict__)
        # 实例化一个将是，存储到讲师文件

    def show_teacher(self):
        print('---查看讲师---')
        name = input("输入查看讲师名：").strip()
        if os.path.exists('%s%s' % (config.teacher, name)):
            teacher = rw.read('%s%s' % (config.teacher, name))
            print('讲师名:%s 所教班级%s' % (teacher['name'], teacher['classes']))
        else:
            print('讲师名输入有误！')

    def create_course(self):
        print('---创建课程---')
        # 输入课程信息，创建课程对象
        name = input("输入课程名:").strip()
        period = input('输入课程周期:').strip()
        price = input('输入课程价格:').strip()
        course = teacher.Course(name, period, price)
        rw.write("%s%s" % (config.course, name), course.__dict__)

    def show_course(self):
        print('---查看科目---')
        # 打开course文件，展示
        name = input("输入查看课程名：").strip()
        if os.path.exists('%s%s' % (config.course, name)):
            course = rw.read('%s%s' % (config.course, name))
            print('课程名:%s 周期%s个月 价格%s' % (course['name'], course['period'], course['price']))
        else:
            print('课程名输入有误！')

    def create_classes(self):
        print('---创建班级---')
        # 输入班级名称、学校、绑定学科
        name = input('输入班级名称：').strip()
        course = input('输入科目名称：').strip()
        area = input('输入城市：').strip()
        classes = teacher.Classes(course, name, area)
        rw.write("%s%s" % (config.classes, name), classes.__dict__)
        # 创建班级文件存学生信息，将路径存入班级对象
        # 创建班级对象（名称 学校 学科 讲师空 学生信息

    def show_classes(self):
        print('---查看班级---')
        # 打开文件
        name = input("输入查看班级名：").strip()
        if os.path.exists('%s%s' % (config.classes, name)):
            classes = rw.read('%s%s' % (config.classes, name))
            print('班级名:%s 所在地%s 老师%s' % (classes['name'], classes['area'], classes['teacher']))
        else:
            print('课程名输入有误！')

    def create_student(self):
        print('---创建学生---')
        # 输入学生用户名密码存入登陆信息到db
        name = input('输入学生姓名：').strip()
        password = input('输入学生密码：').strip()
        config.user_dic[name] = [password, 'student']
        rw.write(config.userinfo, config.user_dic)
        # 实例化一个学生对象（姓名 讲师空表）
        stu = student.Student(name)
        rw.write("%s%s" % (config.student, name), stu.__dict__)

    def show_student(self):
        print('---查看学生---')
        name = input("输入查看学生名：").strip()
        if os.path.exists('%s%s' % (config.student, name)):
            student = rw.read('%s%s' % (config.student, name))
            print('学生名:%s 班级%s 缴费信息%s' % (student['name'], student['classes'], student['pay']))
        else:
            print('姓名输入有误！')

    def boundclass(self):
        print('---创建绑定---')
        # 指定老师还是学生
        kind = input('选择需要操作（1-老师，2-学生）：').strip()
        if int(kind) == 1:
            # 老师添加班级并保存信息,班级增加讲师
            name = input('输入老师姓名：').strip()
            if os.path.exists('%s%s' % (config.teacher, name)):
                teacher.Teacher.choice_classes(name)
            else:
                print('老师姓名错误！')
        elif int(kind) == 2:
            # 学生添加班级并保存信息,班级增加学生姓名。
            name = input('输入学生姓名：').strip()
            if os.path.exists('%s%s' % (config.student, name)):
                student.Student.choice_classes(name)
            else:
                print('学生姓名错误！')
