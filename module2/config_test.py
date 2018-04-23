#!/usr/bin/env python
# -*- coding: utf-8 -*-
import configparser
conf = configparser.ConfigParser()
conf.read("config.ini")
print(conf["group1"]["k2"])
# 添加配置信息
# conf.add_section("group3")
conf["group3"]["name"] = "fans"
conf["group3"]["age"] = "26"
conf["group3"]["character-set-server"] = "utf8"
conf.write(open("config.ini", 'w'))
# 删除配置键值
conf.remove_option("group3", "name")
conf.remove_section("group3")