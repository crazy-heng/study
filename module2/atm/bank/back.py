#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import hashlib
import random
import logging
from logging import handlers
import write
user_dir = "userdata"

#  添加记录购物是否成功日志
logger = logging.getLogger("back")
logger.setLevel(logging.DEBUG)
fh = handlers.TimedRotatingFileHandler("../logs/back.log", when="D", interval=1, backupCount=30, encoding="utf-8")
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger.addHandler(fh)
fh.setFormatter(file_formatter)


def view(dic):  # 显示后台用户信息
    print("""--------user info--------
name:   %s
balance:    %s
cardno: %s
lock: %s
    """ % (dic["name"], dic["balance"], account["card"], dic["lock"]))


user = "admin"
password = "admin"

print("----欢迎登陆**银行后台----")
_username = input("请输入用户名：").strip()
_password = input("请输入密码：").strip()

if _username == user and _password == password:
    logger.info("%s登陆" % _username)
    while True:
        ch = input("请选择操作 1 修改用户 2 新增用户 q退出").strip()
        if ch.isdigit() and ch == '1':
            name = input("请输入用户名：")
            if os.path.exists("%s/%s.log" % (user_dir, name)):
                with open("%s/%s.log" % (user_dir, name), "r", encoding="utf-8") as f:
                    account = eval(f.readline())
                view(account)
                ch1 = input("1-1 修改balance 1-2 解锁或锁定用户").strip()
                if ch1.isdigit() and ch1 == '1':
                    price = input("输入修改金额：").strip()
                    if price.isdigit():
                        account["balance"] = int(price)
                        write.write_account(name, account)
                        logger.info("修改用户%s额度" % name)
                        view(account)
                    else:
                        print("输入错误！")
                elif ch1.isdigit() and ch1 == "2":
                    if account["lock"] == "locked":
                        account["lock"] = "unlock"
                        write.write_account(name, account)
                        logger.info("解锁了用户%s" % name)
                        view(account)
                    elif account["lock"] == "unlock":
                        account["lock"] = "locked"
                        write.write_account(name, account)
                        logger.info("锁定了用户%s" % name)
                        view(account)
                else:
                    print("选择错误！")
            else:
                print("无此用户！")
        elif ch.isdigit() and ch == '2':
            name = input("2-1 输入用户名：").strip()
            user_pass = input("2-2 输入用户密码：").strip()
            balance = input("2-3 输入开卡额度").strip()
            card_no = random.randint(60005000000000, 60009999999999)
            _password_md5 = hashlib.md5()
            _password_md5.update(user_pass.encode(encoding="utf-8"))
            account = {'password': _password_md5.hexdigest(), 'lock': 'unlock', 'name': name, 'card': card_no,
                       'balance': balance}
            view(account)
            logger.info("新增了用户%s" % name)
            write.write_account(name, account)
        elif ch == "q":
            logger.info("%s退出" % _username)
            exit("再见")
        else:
            print("输入错误！")