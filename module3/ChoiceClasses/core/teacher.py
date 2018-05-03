#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from conf import config
from core import rw, student


class Classes:
    school = 'luffycity'

    def __init__(self, course, name, area):
        self.name = name    # 班级名称
        self.area = area    # 城市
        self.course = course  # 科目
        self.teacher = None
        self.student = []


class Course:
    def __init__(self, name, period, price):
        self.name = name    # 课程名
        self.period = period    # 课程周期
        self.price = price  # 课程价格


class Teacher:
    menu = [['查看信息', '1'], ['选择班级', '2'], ['查看学生', '3']]

    def __init__(self, name):
        self.name = name
        self.classes = []
        self.course = []

    def show(self):
        teacher = rw.read('%s%s' % (config.teacher, self))
        print('讲师名:%s 所教班级%s' % (teacher['name'], teacher['classes']))

    def choice_classes(self):
        classes_name = input('请输入班级名：')
        if os.path.exists('%s%s' % (config.classes, classes_name)):
            # 老师信息写入班级
            classes = rw.read('%s%s' % (config.classes, classes_name))
            if not classes['teacher']:
                classes['teacher'] = self
                rw.write('%s%s' % (config.classes, classes_name), classes)
                # 班级信息写入老师表
                teacher = rw.read('%s%s' % (config.teacher, self))
                teacher['classes'].append(classes_name)
                rw.write('%s%s' % (config.teacher, self), teacher)
            else:
                print("班级已有老师！")

        else:
            print('无此班级！')

    def show_student(self):
        stu = []
        teacher = rw.read('%s%s' % (config.teacher, self))
        for i in teacher['classes']:
            c = rw.read('%s%s' % (config.classes, i))
            stu += c['student']
        print('现有学生%s' % stu)
