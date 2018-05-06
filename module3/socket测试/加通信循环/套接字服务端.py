#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.bind(('127.0.0.1', 8080))  # 0-65535 0-1024系统用
phone.listen(5)

print('starting')
conn, client_addr = phone.accept()
print(client_addr)

while True:
    data = conn.recv(1024)  # 单位bytes代表最大接收1024字节
    conn.send(data.upper())

conn.close()
phone.close()
