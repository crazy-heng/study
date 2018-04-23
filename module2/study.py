#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
import time
import random

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


