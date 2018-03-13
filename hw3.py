#!/usr/bin/env python
# -*- coding:utf-8 -*-
goods = [
{"name": "电脑", "price": 1999},
{"name": "鼠标", "price": 10},
{"name": "游艇", "price": 20},
{"name": "美女", "price": 998},
]
user_list = [["fan", "123"], ["alex", "234"], ["li", "456"]]
# 用户登录检测
count = 0
login_flag = False
while count < 3:
    if login_flag:
        break
    user_name = input("请输入用户名：").strip()
    user_pass = input("请输入密码：").strip()
    for user_item in user_list:
        if user_name == user_item[0] and user_pass == user_item[1]:
            print("用户" + user_name + "登录成功！")
            login_flag = True
            break
    else:
        print("用户名密码输入有误！")
    count += 1
else:
    print("输入错误次数过多，稍后重试！")
    exit()
# 用户登录后查询历史购买记录

# 新用户输入工资记录
user_price = int(input("请输入工资："))
while True:
    for item in goods:
        print(item["name"] + " 价格：" + str(item["price"]))
    user_ch = input("请选择所需物品（q退出）：")
    for item in goods:
        if user_ch == item["name"] and user_price > item["price"]:
            user_price = user_price - item["price"]
            print("购买了：" + user_ch + " 余额：" + str(user_price))
            break
        elif user_ch == "q":
            exit()
    else:
        print("选择错误,请重新选择！")
    user_ch = input("是否继续购物？(任意键继续、q退出）")
    if user_ch == "q":
        exit()

