#!/usr/bin/env python
# -*- coding: utf-8 -*-


def view(_username):
    with open("%s.log" % _username, 'r', encoding="utf-8") as f:
        account = eval(f.readline())
    print("""--------user info--------
name:   %s
balance:    %s
cardno: %s
""" % (account["name"], account["balance"], account["card"]))


# view("fan")