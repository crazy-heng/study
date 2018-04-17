#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from bank import b_login


@b_login.login
def pay(_username, price):  # 传入用户账户和消费金额扣款
    with open("../bank/userdata/%s.log" % _username, "r", encoding="utf-8") as f:
        account = eval(f.readline())
    if price > account["balance"]:
        print("余额不足！")
        return False
    else:
        account["balance"] -= price
        with open("../bank/userdata/%s.log" % _username, 'w', encoding="utf-8") as f:
            f.write(str(account))
        print("消费成功")
        return True