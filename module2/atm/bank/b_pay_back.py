#!/usr/bin/env python
# -*- coding: utf-8 -*-
import write


def pay_back(_username):
    price = input("请输入还款金额：").strip()
    if price.isdigit() and int(price) > 0:
        with open("userdata/%s.log" % _username, 'r', encoding="utf-8") as f:
            account = eval(f.readline())
        account["balance"] += int(price)
        print("还款%s成功,当前余额%s!" % (price, account["balance"]))
        write.write_account(_username, account)
        write.blog("pay_back", "用户%s执行了还款操作!" % _username)
        write.log("还款", "info", "用户[%s]还款[%s]" % (_username, price))
    else:
        print("输入有误！")