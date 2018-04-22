#!/usr/bin/env python
# -*- coding: utf-8 -*-
import write


def view(_username):
    with open("userdata/%s.log" % _username, 'r', encoding="utf-8") as f:
        account = eval(f.readline())
    print("""--------user info--------
name:   %s
balance:    %s
cardno: %s
""" % (account["name"], account["balance"], account["card"]))
    write.blog("view", "用户%s执行了查询账户操作！" % _username)