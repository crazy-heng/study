#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
import os
_username = None


def login(func):
    def wrapper(*args, **kwargs):
        global _username
        _password_md5 = hashlib.md5()
        _username = input("请输入银行用户名：").strip()
        _password = input("请输入密码:").strip()
        _password_md5.update(_password.encode(encoding="utf-8"))
        # 导入用户文件成为列表
        account = {}
        if os.path.exists("../bank/%s.log" % _username):
            with open("../bank/%s.log" % _username, "r", encoding="utf-8") as f:
                account = eval(f.readline())
            if account["password"] == _password_md5.hexdigest():
                print("登陆成功,余额%s" % account["balance"])
                func(*args, **kwargs)
                return True
            else:
                print("用户名或密码错误！")
                return False
        else:
            print("用户名或密码错误！")
            return False
    return wrapper

#
# @login
# def pay():
#     print("pay")
#     print(_username)
#
#
# pay()