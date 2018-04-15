#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
_password_md5 = hashlib.md5()
# 导入用户文件成为列表
account = []
with open("user.txt", "r", encoding="utf-8") as f:
    for line in f.readlines():
        account.append(line.strip().split(","))


def login(func):
    def wrapper(*args, **kwargs):
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
                    func(*args, **kwargs)
                    login_flag = True
                    break
            else:
                print("用户名或密码错误")
            i += 1
        else:
            exit("输入错误次数过多！")
    return wrapper


# @login  # name=login(name)
# def cart(k):
#     print("hello", k)
