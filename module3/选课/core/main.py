#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from conf import config
from core import rw, manager


user_dic = eval(rw.read(config.userinfo))
print(user_dic)


def login(func):
    def inner(*args, **kwargs):
        count = 0
        while count < 3:
            user_name = input("请输入用户名：").strip()
            user_pass = input("请输入密码：").strip()
            for user_item in user_dic.keys():
                if user_name == user_item and user_pass == user_dic[user_item][0]:
                    print("用户" + user_name + "登录成功！")
                    func(user_dic[user_item][1])
                    return
            else:
                print("用户名密码输入有误！")
            count += 1
        else:
            print("输入错误次数过多，稍后重试！")
            exit()
    return inner


@login
def main(who):
    '''
    打印欢迎信息
    login得到返回值
    打印对应功能菜单
    通过角色对象去调用
    :return:
    '''
    print(manager.Manager.menu)
    print(who)
