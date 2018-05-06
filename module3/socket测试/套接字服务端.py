#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket

# 1、买手机
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2、绑定手机卡
phone.bind(('127.0.0.1', 8080))  # 0-65535 0-1024系统用

# 3、开机
phone.listen(5)

# 4、等电话
print('starting')
conn, client_addr = phone.accept()

# 5、收发消息
data = conn.recv(1024)  # 单位bytes代表最大接收1024字节
conn.send(data.upper())

# 6、挂电话
conn.close()

# 7、关机
phone.close()
