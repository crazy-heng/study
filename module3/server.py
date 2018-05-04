#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket

HOST = ''
PORT = 50007

sock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_server.bind((HOST, PORT))
sock_server.listen(5)


while True:
    conn, addr = sock_server.accept()
    with conn:
        print('Connect by', addr)
        data = conn.recv(1024)
        print(data.decode())
        while True:
            msg = input('-->>').strip()
            if len(msg) == 0:
                continue
            conn.send(msg.encode())
            data = conn.recv(1024)
            if not data:
                break
            print(data.decode())

            # if not data:
            #     break
            # conn.sendall(data)

