#!/usr/bin/env python
# -*- coding:utf-8 -*-
user_list = [["fan", "123"], ["cai", "234"], ["li", "456"]]
count = 0
login_flag = False
block_flag = 0
block_name = None

f = open("block.log", "r")  # 导入锁定名单到列表block初始为[]
line = f.readline()
block = eval(line)
f.close()

while count < 3:
    if login_flag:
        break   # 登陆成功退出循环

    user_name = input("请输入用户名:").strip()
    user_pass = input("请输入密码:").strip()

    if user_name in block:
        print(u'用户{0:s}已被锁定'.format(user_name))
        exit()

    for user_item in user_list:
        if user_item[0] == user_name and user_item[1] == user_pass:
            print("用户%s登录成功！" % user_name)
            login_flag = True
            break
    else:
        if user_name == block_name:  # 判断前后两次输入用户名是否相同
            block_flag += 1
            if block_flag == 2:  # 相同用户输错三次密码锁定
                block.append(user_name)
                f = open("block.log", "w")
                f.write(str(block))
                f.close()
                print(u"错误3次用户{0:s}已被锁定".format(user_name))
                break
        print("用户名或密码错误，请重新输入！")
        block_name = user_name
    count += 1
