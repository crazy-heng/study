#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import hashlib


def login(func):
    def wrapper(*args, **kwargs):
        _password_md5 = hashlib.md5()
        _username = input("请输入银行用户名：").strip()
        _password = input("请输入银行密码:").strip()
        _password_md5.update(_password.encode(encoding="utf-8"))
        # 导入用户文件成为列表
        account = {}
        if os.path.exists("../bank/userdata/%s.log" % _username):
            with open("../bank/userdata/%s.log" % _username, "r", encoding="utf-8") as f:
                account = eval(f.readline())
            if account["password"] == _password_md5.hexdigest():
                print("登陆成功,余额%s" % account["balance"])
                return func(*args, **kwargs)
            else:
                print("用户名或密码错误！")
        else:
            print("用户名或密码错误！")
    return wrapper


@login
def pay(_username, price):  # 传入用户账户和消费金额扣款
    with open("../bank/userdata/%s.log" % _username, "r", encoding="utf-8") as f:
        account = eval(f.readline())
    if price > account["balance"]:
        print("余额不足！")
        return False
    else:
        account["balance"] -= price
        with open("../bank/userdata/%s.log" % _username, 'w', encoding="utf-8") as f:
            f.write(str(account))
        print("消费成功")
        return True