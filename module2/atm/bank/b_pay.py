#!/usr/bin/env python
# -*- coding: utf-8 -*-
from . import b_login
from . import write


@b_login.login
def pay(_username, price):  # 传入用户账户和消费金额扣款
    with open("%s.log" % _username, "r", encoding="utf-8") as f:
        account = eval(f.readline())
        print(account)
        print(price)
    if price > account["balance"]:
        print("余额不足！")
        return False
    else:
        account["balance"] -= price
        write.write_account(_username, account)
        print("消费成功")
        return True