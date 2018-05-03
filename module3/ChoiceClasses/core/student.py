#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from conf import config
from core import rw


class Student:
    menu = [['查看信息', '1'], ['选择班级', '2'], ['缴费', '3']]

    def __init__(self, name):
        self.name = name
        self.classes = []
        self.pay = {}

    def show(self):
        student = rw.read('%s%s' % (config.student, self))
        print('学生名:%s 所属班级%s 缴费情况%s' % (student['name'], student['classes'], student['pay']))

    def choice_classes(self):
        classes_name = input('请输入班级名：')
        if os.path.exists('%s%s' % (config.classes, classes_name)):
            # 班级写入学生信息
            student = rw.read('%s%s' % (config.student, self))
            if classes_name not in student['classes']:
                student['classes'].append(classes_name)
                rw.write('%s%s' % (config.student, self), student)
                # 学生姓名写入班级
                classes = rw.read('%s%s' % (config.classes, classes_name))
                classes['student'].append(self)
                rw.write('%s%s' % (config.classes, classes_name), classes)
            else:
                print('已经是%s班学生' % classes_name)
        else:
            print('无此班级！')

    def pay(self):
        print('功能开发中')
