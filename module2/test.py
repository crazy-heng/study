#!/usr/bin/env python
# -*- coding:utf-8 -*-
f = open("user.txt", 'r')
raw_data = f.readlines()
accounts = {}
# 把账户数据从文件里读书来，变成dict,这样后面就好查询了
for line in raw_data:
    line = line.strip()
    if not line.startswith("#"):
        items = line.split(",")
        accounts[items[0]] = items[1:]
print(accounts)


# 显示用户信息
def print_user_info(accountdic, username):
    userdic = accountdic[username]
    info = ('''--------userinfo---------
Name:  %s
age:  %s
position:  %s
department:  %s
-------------------------''' % (username, userdic[1], userdic[2], userdic[3]))
    print(info)


username = input("输入查找用户名：")
print_user_info(accounts, username)

for index, v in enumerate(accounts["username"]):
    print(index, v)
