#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import write


def transfer(_username):
    _username1 = input("请输入想转入的账号：").strip()
    price = input("请输入转账金额:").strip()
    if price.isdigit() and int(price) > 0:
        with open("userdata/%s.log" % _username, 'r', encoding="utf-8") as f:
            account = eval(f.readline())
        if os.path.exists("userdata/%s.log" % _username1) and account["name"] != _username1:
            with open("userdata/%s.log" % _username1, 'r', encoding="utf-8") as f:
                account1 = eval(f.readline())
            if account["balance"] > int(price):
                print("向用户%s转账%s" % (_username1, price))
                account["balance"] -= int(price)
                account1["balance"] += int(price)
                print("当前余额%s" % account["balance"])
                write.write_account(_username, account)
                write.write_account(_username1, account1)
                write.log("转账", "info", "用户[%s]转给[%s][%s]" % (_username, _username1, price))
                write.blog("transfer", "用户%s执行了转账操作！" % _username)
                return True
            else:
                print("余额不足%s，无法转账！" % price)
                write.log("转账", "error", "用户[%s]转给[%s]失败！" % (_username, _username1))
                return False
        else:
            print("转入账号错误！")
            return False
    else:
        print("输入有误！")