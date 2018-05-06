#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket

# 1、买手机
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2、打电话
phone.connect(('127.0.0.1', 8080))

# 3、发、收信息
phone.send('hello'.encode('utf-8'))
data = phone.recv(1024)
print(data)

# 4、关闭
phone.close()
