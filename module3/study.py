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

import pickle
import os
import time
import hashlib
import settings


class Mysql:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.id = self.create_id()

    @staticmethod
    def create_id():
        # new_id = 1000000000000 + round(time.time())
        m = hashlib.md5(str(time.time()).encode('utf-8'))
        return m.hexdigest()

    @classmethod
    def from_conf(cls):
        return cls(settings.HOST, settings.PORT)

    def save_id(self):
        print(self.__dict__)
        with open("%s/%s" % (settings.DB_PATH, self.id), 'wb') as f:
            data = self.__dict__
            pickle.dump(data, f)

    def get_obj_by_id(self):
        if os.path.exists("%s/%s" % (settings.DB_PATH, self.id)):
            with open("%s/%s" % (settings.DB_PATH, self.id), 'rb') as f:
                data = pickle.load(f)
            print(data)


# m = Mysql('192.168.1.1', 3306)
# time.sleep(1)
n = Mysql.from_conf()
# print(m.__dict__)
# print(n.__dict__)
# m.Save_id(m)
n.save_id()
n.get_obj_by_id()
