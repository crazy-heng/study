#!/usr/bin/env python
# -*- coding: utf-8 -*-
import write


def pay_back(_username, price):
    with open("%s.log" % _username, 'r', encoding="utf-8") as f:
        account = eval(f.readline())
    account["balance"] += price
    print("还款%s成功,当前余额%s!" % (price, account["balance"]))
    write.write_account(_username, account)


# pay_back("fan", 1500)
