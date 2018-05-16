#!/usr/bin/env python
# -*- coding:utf-8 -*-


# class Student:
#     count = 0
#
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#         Student.count += 1
#
#
# s1 = Student('李坦克', 18, '男')
# s2 = Student('张大炮', 20, '男')
# print("实例化%s个学生" % Student.count)
# print(s1.__dict__)
# print(s1.name)
# print(s2.name)


# class Hero:
#     def __init__(self, name, nick_name, att, blood):
#         self.name = name
#         self.nickname = nick_name
#         self.att = att
#         self.blood = blood
#
#     def hit(self, hero2):
#         hero2.blood -= self.att
#         print("%s攻击%s,%s被打%s剩余血量%s" % (self.nickname, hero2.nickname, hero2.nickname, self.att, hero2.blood))
#         if hero2.blood <= 0:
#             print("%s打败了%s！" % (self.name, hero2.name))
#             res = "deal"
#         else:
#             res = "alive"
#         return res
#
#
# h1 = Hero("张大炮", "炮", 800, 1000)
# h2 = Hero("李坦克", "坦", 200, 3000)
# while True:
#     if h1.hit(h2) == "deal" or h2.hit(h1) == "deal":
#         break

# import pickle
# import os
# import time
# import hashlib
# import settings
# import uuid
#
#
# class Mysql:
#     def __init__(self, host, port):
#         self.host = host
#         self.port = port
#         self.id = self.create_id()
#
#     # def __str__(self):
#     #     return 'test'
#
#     @staticmethod
#     def create_id():
#         my_id = uuid.uuid1()
#         # new_id = 1000000000000 + round(time.time())
#         # m = hashlib.md5(str(time.time()).encode('utf-8'))
#         return str(my_id)
#
#     @classmethod
#     def from_conf(cls):
#         return cls(settings.HOST, settings.PORT)
#
#     def save_id(self):
#         print(self.__dict__)
#         with open("%s/%s" % (settings.DB_PATH, self.id), 'wb') as f:
#             data = self.__dict__
#             pickle.dump(data, f)
#
#     @staticmethod
#     def get_obj_by_id(id):
#         if os.path.exists("%s/%s" % (settings.DB_PATH, id)):
#             with open("%s/%s" % (settings.DB_PATH, id), 'rb') as f:
#                 data = pickle.load(f)
#             print(data)


# m = Mysql('192.168.1.1', 3306)
# time.sleep(1)
# n = Mysql.from_conf()
# print(n.__dict__)
# print(m.__dict__)
# print(n.__dict__)
# m.Save_id(m)
# n.save_id()
# Mysql.get_obj_by_id('01d68ec8-58c1-11e8-80ae-005056c00008')


# class People(object):
#     __name = "luffy"
#     __age = 18
#
#
# p1 = People()
# print(p1._People__name, p1._People__age)

# 5-8
class Mysql:
    def __init__(self, host, port, db, charset):
        self.host = host
        self.port = port
        self.db = db
        self.charset = charset
        self.conn = connect(self.host, self.port, self.db, self.charset)

    def exc1(self, sql):
        return self.conn.execute(sql)

    def exec2(self, sql):
        return self.conn.call_proc(sql)


# 5-10
class People(object):
    def __init__(self):
        print("__init__")

    def __new__(cls, *args, **kwargs):
        print("__new__")
        return object.__new__(cls, *args, **kwargs)


People()


# 5-11
class A(object):

    def foo(self, x):
        print("executing foo(%s, %s)" % (self, x))

    @classmethod
    def class_foo(cls, x):
        print("executing class_foo(%s, %s)" % (cls, x))

    @staticmethod
    def static_foo(x):
        print("executing static_foo(%s)" % x)


a = A()
a.foo(1)
a.class_foo(2)
a.static_foo(3)


# 5-12
class Dog(object):

    def __init__(self, name):
        self.name = name

    @property
    def eat(self):
        print(" %s is eating" % self.name)


d = Dog("ChenRonghua")
d.eat


# 5-22
import json


class Myclass:
    def __init__(self, name, password, status, timeout):
        self.name = name
        self.password = password
        self.status = status
        self.timeout = timeout

    def save(self):
        data = {
            self.name: {
                "password": self.password,
                'status': self.status,
                'timeout': self.timeout}}
        with open(self.name, 'w') as f:
            json.dump(data, f)

    @property
    def db(self):
        with open(self.name, 'r') as f:
            print(json.load(f))


egon = Myclass('egon', '123', 'False', 0)
egon.save()
egon.db