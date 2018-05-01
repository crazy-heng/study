#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 管理员类


class Manager:
    menu = {'创建讲师账号': '', '创建学生账号': '', '创建课程': '', '创建班级': '', '创建班级绑定': '', '查看讲师账号': '',
            '查看学生账号': '', '查看课程': '', '查看班级': ''}

    def __init__(self, name):
        self.name = name

    def creat_t(self):
        # 输入老师用户名密码存入登陆信息到db
        # 输入老师所在学校 用户名 身份 学校
        # 实例化一个将是，存储到讲师文件
        pass

    def creat_c(self):
        # 输入课程信息，创建课程对象
        pass

    def show_c(self):
        # 打开course文件，展示
        pass

    def create_classes(self):
        # 输入班级名称、学校
        # 绑定学科
        # 创建班级文件存学生信息，将路径存入班级对象
        # 创建班级对象（名称 学校 学科 讲师空 学生信息路径
        pass

    def show_classes(self):
        # 打开文件
        # 读出信息
        pass

    def creat_s(self):
        # 输入学生用户名密码存入登陆信息到db
        # 实例化一个学生对象（姓名 讲师空表）
        pass

    def boundclass(self):
        # 指定老师还是学生
        # 老师1查看老师对应班级2添加一个新班级3班级的属性里加入老师
        # 学生1查看所属班级2学生加入新班级3班级存储学生信息
        pass