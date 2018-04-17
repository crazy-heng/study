#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
import os
import b_draw
import b_pay_back
import b_transfer
import b_view
import write
_username = None


def login(func):  # 银行用户登陆验证
    def wrapper(*args, **kwargs):
        global _username
        _password_md5 = hashlib.md5()
        _username = input("请输入银行用户名：").strip()
        _password = input("请输入银行密码:").strip()
        _password_md5.update(_password.encode(encoding="utf-8"))
        # 导入用户文件成为列表
        if os.path.exists("../bank/userdata/%s.log" % _username):
            with open("../bank/userdata/%s.log" % _username, "r", encoding="utf-8") as f:
                account = eval(f.readline())
            if account["lock"] == "locked":
                print("账号被锁定！")
                return False
            elif account["password"] == _password_md5.hexdigest():
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


@login
def main():
    name = _username
    write.blog("login", "用户%s登陆了系统！" % name)
    while True:
        ch = input("欢迎进入银行后台！请选择操作内容：1查询 2取现 3转账 4还款 q退出").strip()
        if ch.isdigit() and ch == "1":
            b_view.view(name)
            write.blog("view", "用户%s执行了查询账户操作！" % name)
        elif ch.isdigit() and ch == "2":
            price = input("请输入取现金额：").strip()
            if price.isdigit() and int(price) > 0:
                b_draw.draw(name, int(price))
                write.blog("draw", "用户%s执行了取现操作！" % name)
            else:
                print("输入有误！")
        elif ch.isdigit() and ch == "3":
            name1 = input("请输入想转入的账号：").strip()
            price = input("请输入转账金额:").strip()
            if price.isdigit() and int(price) > 0:
                b_transfer.transfer(name, name1, int(price))
                write.blog("transfer", "用户%s执行了转账操作！" % name)
            else:
                print("输入有误！")
        elif ch.isdigit() and ch == "4":
            price = input("请输入还款金额：").strip()
            if price.isdigit() and int(price) > 0:
                b_pay_back.pay_back(name, int(price))
                write.blog("pay_back", "用户%s执行了还款操作!" % name)
            else:
                print("输入有误！")
        elif ch == 'q':
            write.blog("exit", "用户%s退出登录！" % name)
            exit("欢迎下次登陆！")
        else:
            print("输入错误！")


if __name__ == "__main__":
    main()