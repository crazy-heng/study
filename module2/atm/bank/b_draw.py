#!/usr/bin/env python
# -*- coding: utf-8 -*-
import write


def draw(_username):
    price = input("请输入取现金额：").strip()
    if price.isdigit() and int(price) > 0:
        with open("userdata/%s.log" % _username, 'r', encoding="utf-8") as f:
            account = eval(f.readline())
        if account["balance"] > int(price)*1.05:
            print("提现[%s]，手续费[%s]" % (price, int(price)*0.05))
            account["balance"] -= int(price) * 1.05
            write.write_account(_username, account)
            write.log("提现", "info", "用户[%s]提现[%s]手续费[%s]" % (_username, price, int(price)*0.05))
            print("当前余额：[%s]" % account["balance"])
            write.blog("draw", "用户%s执行了取现操作！" % _username)
        else:
            print("余额不足[%s]无法提现！" % price)
            write.blog("draw", "用户%s提现失败!" % _username)
    else:
        print("输入有误！")