#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket

HOST = '127.0.0.1'
PORT = 50007

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
# client.send(b'hello world')

while True:
    msg = input('-->>').strip()
    if len(msg) == 0:
        continue
    client.sendall(msg.encode())
    data = client.recv(1024)
    print('Received', data.decode())