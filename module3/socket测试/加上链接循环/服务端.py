#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
phone.bind(('127.0.0.1', 8081))  # 0-65535 0-1024系统用
phone.listen(5)

print('starting')
while True:  # 链接循环不断提供服务
    conn, client_addr = phone.accept()
    print(client_addr)

    while True:
        try:
            data = conn.recv(1024)  # 单位bytes代表最大接收1024字节,
            if not data:  # linux收不到会死循环
                break
            print('客户端数据', data)
            conn.send(data.upper())
        except ConnectionResetError:  # windows系统用try处理客户端断开报错退出
            break
    conn.close()

phone.close()
