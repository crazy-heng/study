#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
import time
import random
import json
import random
import string
import logging
from logging import handlers
import hashlib
import sys
import os
import configparser
import xml.etree.ElementTree as ET

# 函数1
# def sum_nu(*args):
#     a = 0
#     for i in args:
#         a += i
#     print(a)
#
#
# sum_nu(1, 2, 3, 4, 5)


# 函数2
# def replace_file(name, old_content, new_content):
#     f = open(name, 'r')
#     f1 = f.read()
#     f.close()
#     f1 = re.sub(old_content, new_content, f1)
#     f = open(name, 'w')
#     f.write(f1)
#     f.close()
#
#
# replace_file("test.txt", "HEHE", "new")


# 函数3
# def check(a):
#     print("wrong") if len(a) == 0 else print(a)
#
#
# check("")

# 函数4
# def check_dic(d, long):
#     for i in d.keys():
#         if len(d[i]) > long:
#             d[i] = d[i][:long]
#     print(d)
#
#
# dic = {"k1": "v1v1", "k2": [11, 22, 33, 44]}
# check_dic(dic, 1)


# def cal(num):
#     j = 1
#     for i in range(1, num+1):
#         j *= i
#     print(j)
#
# cal(5)


# def logger(filename, channel='file'):
#     for i in range(10000):
#         if channel == 'file':
#             pass
#         elif channel == 'terminel':
#             data = yield
#             i += 1
#             print(time.strftime("%Y-%m-%d %X") + " [%s] %s" % (i, data))
#
#
# log_obj = logger(filename="web.log", channel='terminel')
# log_obj.__next__()
# log_obj.send('user alex login success')
# log_obj.send('user alex login success')


# name = ['alex', 'wupeiqi', 'yuanhao', 'nezha']
# new_name = map(lambda x: x + "_sb", name)
# print(list(new_name))
# print(sorted(name, key=lambda x: x[1], reverse=True))


# num = [1, 3, 5, 6, 7, 8]  # 取偶数
# print(list(filter(lambda x: x % 2 == 0, num)))

# li = ['alex', 'egon', 'smith', 'pizza', 'alen']
# index = 0
# for i in li:
#     if i[0] == "a":
#         li[index] = i.capitalize()
#     index += 1
# print(li)


# def roll_dice(numbers=3, points=None):
#     """
#      定义骰子，循环三次
#     :param numbers:
#     :param points:
#     :return:
#     """
#
#     print('----- 摇骰子 -----')
#     if points is None:
#         points = []
#     while numbers > 0:
#         point = random.randrange(1, 7)
#         points.append(point)
#         numbers -= 1
#     return points
#
#
# def roll_result(total):
#     """
#     定义大小，三个大或者一个小两个大。三个小或者两个小一个大
#     :param total:
#     :return:
#     """
#
#     is_big = 11 <= total <= 18
#     is_small = 3 <= total <= 10
#     if is_big:
#         return "大"
#     elif is_small:
#         return "小"
#
#
# def start_game():
#     your_money = 1000
#     while your_money > 0:
#         print('----- 游戏开始 -----')
#         choices = ["大", "小"]
#         your_choice = input("请下注， 大 or 小")
#         your_bet = input("下注金额：")
#         if your_choice in choices:
#             points = roll_dice()
#             total = sum(points)
#             you_win = your_choice == roll_result(total)
#             if you_win:
#                 your_money = your_money + int(your_bet)
#                 print("骰子点数", points)
#                 print("恭喜， 你赢了%s元， 你现在的本金%s 元" % (your_bet, your_money))
#             else:
#                 your_money = your_money - int(your_bet)
#                 print("骰子点数", points)
#                 print("很遗憾， 你输了%s元， 你现在的本金%s 元" % (your_bet, your_money))
#         else:
#             print('格式有误，请重新输入')
#     else:
#         print("game over")
#
#
# start_game()

# a = '''<!DOCTYPE html>
# <html lang="en">
# <head>
#    <meta charset="UTF-8">
#    <title>luffycity.com</title>
# </head>
# <body>
# </body>
# </html>'''
# # with open("test.xml", 'r', encoding="utf-8") as f:
# #     data = f.read()
# #     print(data)
# print(re.findall("l\w+.com", a))

# li = {"expire_date": "2021-01-01", "id": 1234, "status": 0, "pay_day": 22, "password": "abc"}
# with open("test.json", 'w') as f:
#     json.dump(li, f)
# with open("test.json", 'r') as f:
#     data = json.load(f)
# print(data)
#
# res = random.sample(string.ascii_lowercase + string.ascii_uppercase + string.digits, 6)
# print(''.join(res))

# logger = logging.getLogger("test")
# logger.setLevel(logging.DEBUG)
# fh = handlers.RotatingFileHandler("web.log", maxBytes=1000, backupCount=3)
# logger.addHandler(fh)
# log_format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
# fh.setFormatter(log_format)
# logger.debug("test")


# with open("test.json", 'r', encoding="utf-8") as f:
#     data = json.load(f)
# md5 = hashlib.md5()
# md5.update(data["password"].encode(encoding="utf-8"))
# data["password"] = md5.hexdigest()
# with open("test.json", 'w') as f:
#     json.dump(data, f)


# print(sys.argv[1])

# 扑克列表
# def cards():
#     puk, num = [], []
#     t = ["红心", "草花", "黑桃", "方块"]
#     for i in range(2, 11):
#         num.append(str(i))
#     num.extend(["J", "Q", "K", "A"])
#     for i in num:
#         for j in t:
#             puk.append(j + i)
#     return puk
#
#
# print(cards())


# def min_max(*args):
#     min_num = args[0]
#     max_num = args[0]
#     for i in args:
#         if i > max_num:
#             max_num = i
#         elif i < min_num:
#             min_num = i
#     print("MAX %s MIN %s" % (max_num, min_num))
#
#
# min_max(1, 8, 3, 999, 43, -1.6)

# print(os.path.dirname(os.path.abspath("study.py")))
# print(os.path.abspath("study.py"))

# conf = configparser.ConfigParser()
# conf.read("my.cnf")
# conf.set("DEFAULT", "character-set-server", "utf-8")
# # conf.set("mysqld", "default-time-zone", "+00:00")
# # conf.set("client", "port", "3306")
# # conf.remove_option("client", "port")
# conf.write(open('my.cnf', "w"))
# print(conf.sections())
# print(conf["mysqld"]["default-time-zone"])

# print(time.strftime("%Y-%m-%d"))
# ex_time = time.mktime(time.strptime("2011-01-01", "%Y-%m-%d"))
# if ex_time > time.time():
#     print("没过期！")
# else:
#     print("已过期！")

# logger = logging.getLogger("access")
# logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
# logger.error('account [1234] too many login attempts')