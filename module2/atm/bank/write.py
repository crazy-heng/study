#!/usr/bin/env python
# -*- coding: utf-8 -*-


def write_account(name, account):
    with open("%s.log" % name, 'w', encoding="utf-8") as f:
        f.write(str(account))