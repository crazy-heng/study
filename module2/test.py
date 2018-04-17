#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 把账户数据从文件里读书来，变成dict,这样后面就好查询了
f = open("user.txt", 'r')
data = f.readline()
accounts = eval(data)
f.close()
print(accounts)


# 修改信息写回文件
def write_txt(account_dic):
    file = open("user.txt", 'w', encoding='utf-8')
    file.write(str(account_dic))
    file.close()


# 显示用户信息
def print_user_info(account_dic, _user_name):
    user_dic = account_dic[_user_name]
    info = ('''--------user_info---------
Name:  %s
age:  %s
position:  %s
department:  %s
-------------------------''' % (_user_name, user_dic[1], user_dic[2], user_dic[3]))
    print(info)


# 修改用户信息ok
def modify_user_info(account_dic, _user_name):
    user_dic = account_dic[_user_name]
    while True:
        for K, V in enumerate(accounts["username"]):
            print(K, V)
        ch = input("选择需要修改的内容:").strip()
        if ch.isdigit() and 0 <= int(ch) < len(user_dic):
            new = input("原内容[%s],输入新内容:" % (user_dic[int(ch)]))
            user_dic[int(ch)] = new
            accounts[_user_name] = user_dic
            write_txt(accounts)
            print("已修改用户[%s]的%s为%s" % (_user_name, accounts["username"][int(ch)], new))
            break
        else:
            print("输入有误,请选择编号！")


_user_name = input("输入要查找用户名：").strip()
if _user_name in accounts.keys():
    print_user_info(accounts, _user_name)
    choice = input("是否要修改用户信息（y确认，任意键退出）：")
    modify_user_info(accounts, _user_name) if choice == "y" else exit("bye!")
else:
    print("无此用户！bye！")


