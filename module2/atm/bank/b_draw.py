#!/usr/bin/env python
# -*- coding: utf-8 -*-
import b_conroller
import write


# @b_conroller.login
def draw(_username, price):
    with open("%s.log" % _username, 'r', encoding="utf-8") as f:
        account = eval(f.readline())
    if account["balance"] > int(price*1.05):
        print("提现[%s]，手续费[%s]" % (price, price*0.05))
        account["balance"] -= (price * 1.05)
        write.write_account(_username, account)
        print("当前余额：[%s]" % account["balance"])
        return True
    else:
        print("余额不足[%s]无法提现！" % price)
        return False


# draw("fan", 100)