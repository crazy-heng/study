#!/usr/bin/env python
# -*- coding:utf-8 -*-
import client
import tools
import setting

print('用户名密码列表存配额 user_dic = {fan: [md5, 100000]}密码md5加密')
user_dic = tools.read('userlist')


def login(func):
    def inner(*args, **kwargs):
        count = 0
        while count < 3:
            user_name = input("请输入用户名：").strip()
            user_pass = input("请输入密码：").strip()
            for user_item in user_dic.keys():
                if user_name == user_item and tools.md5_user(user_pass.encode('utf-8')) == user_dic[user_item][0]:
                    print("用户" + user_name + "登录成功！")
                    func(user_name, user_dic)
                    return
            else:
                print("用户名密码输入有误！")
            count += 1
        else:
            print("输入错误次数过多，稍后重试！")
            exit()
    return inner


@login
def main(user_name, user_info):
    try:
        client.FTPClient((setting.address, int(setting.port)), user_name, user_info).run()
    except Exception as e:
        print(e)
        print('服务器地址或端口错误！')


if __name__ == '__main__':
    main()
