#!/usr/bin/env python
# -*- coding: utf-8 -*-
from concurrent.futures import ThreadPoolExecutor
from socket import *
# from threading import Thread


def communicate(conn):
    while True:
        try:
            data = conn.recv(1024)
            if not data:break
            conn.send(data.upper())
        except ConnectionResetError:
            break

    conn.close()


def server(ip, port):
    server = socket(AF_INET, SOCK_STREAM)
    server.bind((ip, port))
    server.listen(5)

    while True:
        conn, addr = server.accept()
        print(addr)
        # t = Thread(target=communicate, args=(conn,))
        # t.start()
        pool.submit(communicate, conn)

    server.close()


if __name__ == '__main__':
    pool = ThreadPoolExecutor(2)
    server('127.0.0.1', 8081)