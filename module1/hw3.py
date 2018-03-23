#!/usr/bin/env python
# -*- coding:utf-8 -*-
goods = [{"name": "电脑", "price": 1999}, {"name": "鼠标", "price": 10}, {"name": "游艇", "price": 20},
         {"name": "美女", "price": 998}]
user_list = [["fan", "123"], ["alex", "234"], ["li", "456"]]
# 用户登录检测
count = 0
login_flag = False
name = None
while count < 3:
    if login_flag:
        break
    user_name = input("请输入用户名：").strip()
    user_pass = input("请输入密码：").strip()
    for user_item in user_list:
        if user_name == user_item[0] and user_pass == user_item[1]:
            print("用户" + user_name + "登录成功！")
            name = user_name
            login_flag = True
            break
    else:
        print("用户名密码输入有误！")
    count += 1
else:
    print("输入错误次数过多，稍后重试！")
    exit()

user_ch1 = 0
d = {}
d_last = {}
d_history = {}
# 用户登录后查询历史余额
f = open("user.log", "r")
for line in f:
    if line == '\n':
        break
    else:
        d = eval(line)
        # line = line.replace("{", '').replace("}", '').strip().replace("'", '').replace(",", ':').replace(" ", '')\
        #     .split(":")
        # i = j = 0
        # while i < (len(line) // 2):
        #     i += 1
        #     d[line[j]] = line[j+1]
        #     j += 2
f.close()
# 查询用户上次购买物品
f = open("last.log", "r", encoding="utf-8")
for line in f:
    if line == '\n':
        break
    else:
        d_last = eval(line)
f.close()
# 查询用户历史购物记录
f = open("history.log", "r", encoding="utf-8")
for line in f:
    if line == '\n':
        break
    else:
        d_history = eval(line)
f.close()
if d.get(name):
    user_price = int(d[name])
    if d_last.get(name):
        print('\033[1;31;40m' + "上次购买了" + d_last[name] + ",当前余额：" + str(user_price) + '\033[0m')
    else:
         print('\033[1;31;40m' + "上次没有购买,当前余额：" + str(user_price) + '\033[0m')
else:
    # 新用户输入工资记录
    while True:
        price = input("请输入工资：")
        if price.isdigit():
            user_price = int(price)
            print('\033[1;31;40m' + "当前余额：" + str(user_price) + '\033[0m')
            break
        else:
            print("输入工资错误！")

while user_ch1 != "q":
    for item in goods:
        print(item["name"] + " 价格：" + str(item["price"]))
    user_ch = input("请选择所需购买物品（q退出）：")
    for item in goods:
        if user_ch == item["name"] and user_price >= item["price"]:
            user_price = user_price - item["price"]
            print('\033[1;31;40m' + "购买了：" + user_ch + " 余额：" + str(user_price) + '\033[0m')
            # 更新用户和余额文档存储
            d[name] = user_price
            f = open("user.log", "w")
            f.write(str(d) + '\n')
            f.close()
            # 更新用户最后一次购买文档存储
            d_last[name] = user_ch
            f = open("last.log", "w", encoding="utf-8")
            f.write(str(d_last) + '\n')
            f.close()
            # 更新用户历史购买文档存储
            if d_history == {} or name not in d_history.keys():
                d_history[name] = user_ch
                f = open("history.log", "w", encoding="utf-8")
                f.write(str(d_history) + '\n')
                f.close()
            else:
                d_history[name] = str(user_ch) + "*" + d_history[name]
                f = open("history.log", "w", encoding="utf-8")
                f.write(str(d_history) + '\n')
                f.close()
            break
        elif user_ch == item["name"] and user_price < item["price"]:
            print('\033[1;31;40m' + "余额不足，无法购买" + '\033[0m')
        elif user_ch == "q":
            d[name] = user_price
            f = open("user.log", "w")
            f.write(str(d) + '\n')
            f.close()
            exit()
    else:
        print("选择错误,请重新选择！")
    user_ch1 = input("是否继续购物？(任意键继续、q退出）")

else:
    print("购买历史：" + '\033[1;31;40m' + d_history[name] + '\033[0m')