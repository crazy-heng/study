#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Classes:
    def __init__(self, school, name, kind):
        self.school = school  # 学校
        self.name = name    # 班级名称
        self.kind = kind    # 班级科目
        self.student = ['student_obj']


class Course:
    def __init__(self, name, period, price):
        self.name = name    # 课程名
        self.period = period    # 课程周期
        self.price = price  # 课程价格


class Teacher:
    def __init__(self, name, classes, course):
        self.name = name
        self.classes = ['classes_obj']
        self.course = []
