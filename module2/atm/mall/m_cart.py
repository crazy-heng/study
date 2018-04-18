#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import hashlib
import logging
from logging import handlers
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from bank import b_pay

goods = [{"name": "电脑", "price": 1999}, {"name": "鼠标", "price": 10},
         {"name": "游艇", "price": 20}, {"name": "美女", "price": 998}]
name = None
#  添加记录购物是否成功日志
logger = logging.getLogger("cart")
logger.setLevel(logging.DEBUG)
fh = handlers.TimedRotatingFileHandler("../logs/cart.log", when="D", interval=1, backupCount=30, encoding="utf-8")
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger.addHandler(fh)
fh.setFormatter(file_formatter)


def login(func):
    def wrapper(*args, **kwargs):
        global name
        _password_md5 = hashlib.md5()
        # 导入用户文件成为列表
        account = []
        with open("user.txt", "r", encoding="utf-8") as f:
            for line in f.readlines():
                account.append(line.strip().split(","))
        i = 0
        login_flag = False
        while i < 3:
            if login_flag:
                break
            _username = input("请输入用户名：").strip()
            _password = input("请输入密码：").strip()
            _password_md5.update(_password.encode(encoding="utf-8"))
            for k in account:
                if k[0] == _username and k[1] == _password_md5.hexdigest():
                    print("登陆成功！")
                    name = _username
                    func(*args, **kwargs)
                    login_flag = True
                    break
            else:
                print("用户名或密码错误")
            i += 1
        else:
            exit("输入错误次数过多！")
    return wrapper


def buy_list(user, data):  # 购物历史写入文件
    print(data)
    f = open("userdata/%s.txt" % user, 'w+', encoding="utf-8")
    f.write(str(data))
    f.close()


@login
def cart():  # 购物操作
    price = 0
    li = []
    # 判断是否有历史购物记录
    if os.path.exists("userdata/%s.txt" % name):
        with open("userdata/%s.txt" % name, 'r', encoding="utf-8") as file:
            data = eval(file.readline())
    else:
        file = open("userdata/%s.txt" % name, 'w+', encoding="utf-8")
        data = []
        file.write(str(data))
        file.close()
    while True:
        for index, items in enumerate(goods):
            print("%s %s %s" % (index, items["name"], items["price"]))
        ch = input("请选择需要购买物品（p查看结算购物车、c清空购物车、q退出）:").strip()
        if ch.isdigit() and 0 <= int(ch) < len(goods):
            li.append(ch)
            price += goods[int(ch)]["price"]
            print("%s已加入购物车,当前消费\033[31;1m%s\033[0m" % (goods[int(ch)]["name"], price))
            data.append(goods[int(ch)]["name"])
        elif ch == "p":
            print("----当前购物车----")
            for index, items in enumerate(goods):
                print("物品[%s]已购数量[%s]" % (items["name"], li.count(str(index))))
            print("消费总额：消费\033[31;1m[%s]\033[0m" % price)
            # 调用信用卡接口,扣费成功后写文件，不成功则退出
            b_pay_status = b_pay.pay(name, price)
            if b_pay_status:
                buy_list(name, data)
                logger.info("用户%s购物花费%s成功！" % (name, price))
                exit("购物成功！")
            else:
                logger.error("用户%s购物花费%s,结算失败！" % (name, price))
                print("信用卡消费失败！")
        elif ch == "q":
            exit()
        elif ch == "c":
            with open("userdata/%s.txt" % name, 'r', encoding="utf-8") as f:
                data = eval(f.readline())
            price = 0
            li = []
        else:
            print("输入有误，请重新选择!")


if __name__ == "__main__":
    cart()