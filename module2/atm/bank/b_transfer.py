#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import write


def transfer(_username, _username1, price):
    with open("%s.log" % _username, 'r', encoding="utf-8") as f:
        account = eval(f.readline())
    if os.path.exists("%s.log" % _username1):
        with open("%s.log" % _username1, 'r', encoding="utf-8") as f:
            account1 = eval(f.readline())
        if account["balance"] > price:
            print("向用户%s转账%s" % (_username1, price))
            account["balance"] -= price
            account1["balance"] += price
            print("当前余额%s" % account["balance"])
            write.write_account(_username, account)
            write.write_account(_username1, account1)
            write.log("转账", "info", "用户[%s]转给[%s][%s]" % (_username, _username1, price))
            return True
        else:
            print("余额不足%s，无法转账！" % price)
            write.log("转账", "error", "用户[%s]转给[%s]失败！" % (_username, _username1))
            return False
    else:
        print("对方账户不存在！")
        return False


# transfer("fan", "cai", 5000)