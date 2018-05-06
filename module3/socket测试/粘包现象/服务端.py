#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import subprocess

server= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# phone.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('127.0.0.1', 9000))  # 0-65535 0-1024系统用
server.listen(5)

conn, addr = server.accept()

res1 = conn.recv(1)
print('1', res1)

res2 = conn.recv(1024)
print('2', res2)