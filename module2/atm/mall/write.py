#!/usr/bin/env python
# -*- coding: utf-8 -*-


def buy_list(user, data):  # 购物历史写入文件
    f = open("userdata/%s.txt" % user, 'w+', encoding="utf-8")
    f.write(str(data))
    f.close()