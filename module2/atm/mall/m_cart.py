#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import logging
from logging import handlers
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from bank import b_pay
from mall import m_login

goods = [{"name": "电脑", "price": 1999}, {"name": "鼠标", "price": 10},
         {"name": "游艇", "price": 20}, {"name": "美女", "price": 998}]

#  添加记录购物是否成功日志
logger = logging.getLogger("cart")
logger.setLevel(logging.DEBUG)
fh = handlers.TimedRotatingFileHandler("../logs/cart.log", when="D", interval=1, backupCount=30, encoding="utf-8")
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger.addHandler(fh)
fh.setFormatter(file_formatter)


def buy_list(name, data):  # 购物历史写入文件
    print(data)
    f = open("%s.txt" % name, 'w+', encoding="utf-8")
    f.write(str(data))
    f.close()


@m_login.login
def cart(name):  # 购物操作
    price = 0
    li = []
    with open("%s.txt" % name, 'r', encoding="utf-8") as f:
        data = eval(f.readline())
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
            with open("%s.txt" % name, 'r', encoding="utf-8") as f:
                data = eval(f.readline())
            price = 0
            li = []
        else:
            print("输入有误，请重新选择!")


# cart("fan")