#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.connect(('127.0.0.1', 8081))

while True:
    # 1 发命令
    cmd = input('-->').strip()
    if not cmd:
        continue
    phone.send(cmd.encode('utf-8'))

    # 2 拿命令结果
    data = phone.recv(1024)  # 1024一个坑
    print(data.decode('gbk'))  # linux用utf-8解码，windows用gbk解码

phone.close()
