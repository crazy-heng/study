#!/usr/bin/env python
# -*- coding:utf-8 -*-
user_list = [["fan", "123"], ["zhang", "234"], ["li", "456"]]
count = 0
block = []
login_flag = False
block_flag = 0
block_name = None

f = open("block.log", "r")  #导入锁定名单到列表block
line = f.readline()
while line:
    block.append(line.strip('\n'))
    line = f.readline()
f.close()

while count < 3:
    if login_flag:
        break   #登陆成功退出循环

    user_name = input("请输入用户名:").strip()
    user_pass = input("请输入密码:").strip()

    if user_name in block:
        print(u'用户{0:s}已被锁定'.format(user_name))
        exit()

    for user_item in user_list:
        if user_item[0] == user_name and user_item[1] == user_pass:
            print("登录成功！用户" + user_name)
            login_flag = True
            break
    else:
        if user_name == block_name:  #判断是否连续输入三次相同的用户名
            block_flag += 1
            if block_flag == 2:  #相同用户输错三次密码锁定
                f = open("block.log", "a")
                f.write(user_name + '\n')
                f.close()
                print(u"错误3次用户{0:s}已被锁定".format(user_name))
        print("用户名或密码错误，请重新输入！")
        block_name = user_name

    count += 1



# f = open("block.log", "r")
# line = f.readline()
# while line:
#     line=line.strip("\n")
#     if i==line:
#         print("用户已锁定")
#         exit()
#     line = f.readline()
# f.close()
#
# if i in D:
#     print(D[i])
#     l = input("请输入密码:")
#     if l == D[i]:
#         print("用户"+i+"登录成功！")
#     else:
#         for n in range(2):
#             print ("用户"+i+"密码输入错误")
#             l = input("请重新输入密码:")
#             if l == D[i]:
#                 print("用户"+i+"登录成功！")
#                 break
#         print("输错3次账户"+i+"被锁定")
#         f = open("block.log","a")
#         f.write(i+'\n')
#         f.close()
# else:
#     print("无此用户")
# #
# #
#
#
#
