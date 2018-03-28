#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
goods = [{"name": "电脑", "price": 1999}, {"name": "鼠标", "price": 10}, {"name": "游艇", "price": 20},
         {"name": "美女", "price": 998}]
user_list = [["fan", "123"], ["alex", "234"], ["li", "456"]]
# 用户登录检测
count = 0
login_flag = False
_name = ""
while count < 3:
    if login_flag:
        break
    user_name = input("请输入用户名：").strip()
    user_pass = input("请输入密码：").strip()
    for user_item in user_list:
        if user_name == user_item[0] and user_pass == user_item[1]:
            print("用户" + user_name + "登录成功！")
            _name = user_name
            login_flag = True
            break
    else:
        print("用户名密码输入有误！")
    count += 1
else:
    print("输入错误次数过多，稍后重试！")
    exit()

# 判断用户余额，没有则输入工资并创建用户表
Base_Dir = "use_data"
data = {}
if os.path.exists("%s/%s" % (Base_Dir, _name)):
    f = open("%s/%s" % (Base_Dir, _name))
    data = eval(f.read())
else:
    while data == {}:
        balance = input("请输入工资：")
        if balance.isdigit() and int(balance) > 0:
            f = open("%s/%s" % (Base_Dir, _name), 'w')
            data = {"name": _name, "price": int(balance), "cart": []}
            f.write(str(data))
            f.close()
        else:
            print("输入错误请输入正确金额！")
# 提示用户最后购买物品和余额
if len(data["cart"]) > 0:
    print("最近一次购物[%s]，余额[\033[31;1m%s\033[0m]" % (data["cart"][-1]["name"], data["price"]))
else:
    print("现有余额[\033[31;1m%s\033[0m]" % (data["price"]))
# 用户开始购物
while True:
    for index, item in enumerate(goods):
        print("%s.%s %s" % (index, item["name"], item["price"]))
    choice = input("请选择商品购买（q退出）：").strip()
    if choice.isdigit():
        choice = int(choice)
        if 0 <= choice < len(goods):
            ch_item = goods[choice]
            if ch_item["price"] < data["price"]:
                data["cart"].append(ch_item)
                data["price"] -= ch_item["price"]
                print("已添加[%s]到您的购物车，您的余额还有[\033[31;1m%s\033[0m]" % (ch_item["name"], data["price"]))
            else:
                print("余额%s不足以购买[%s]！" % (data["price"], ch_item["name"]))
        else:
            print("输入错误序号！")
    elif choice == "q":
        print("已购买商品".center(50, '-'))
        for index, item in enumerate(data["cart"], 1):
            print("%s %s %s" % (index, item["name"], item["price"]))
        print("你的余额还有[\033[31;1m%s\033[0m]" % (data["price"]))
        # 购物清单和余额存档
        f = open("%s/%s" % (Base_Dir, _name), "w")
        f.write(str(data))
        f.close()
        exit("Bye.")
    else:
        print("请输入序号！")
