#!/usr/bin/env python
# -*- coding: utf-8 -*-
import write


def draw(_username, price):
    with open("%s.log" % _username, 'r', encoding="utf-8") as f:
        account = eval(f.readline())
    if account["balance"] > int(price*1.05):
        print("提现[%s]，手续费[%s]" % (price, price*0.05))
        account["balance"] -= (price * 1.05)
        write.write_account(_username, account)
        write.log("提现", "info", "用户[%s]提现[%s]手续费[%s]" % (_username, price, price*0.05))
        print("当前余额：[%s]" % account["balance"])
        return True
    else:
        print("余额不足[%s]无法提现！" % price)
        write.log("用户%s提现失败!" % _username)
        return False