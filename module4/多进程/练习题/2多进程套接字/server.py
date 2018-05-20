#!/usr/bin/env python
# -*- coding: utf-8 -*-
from socket import *
from multiprocessing import Process


def talk(conn):
    while True:
        try:
            data = conn.recv(1024)
            conn.send(data.upper())
        except ConnectionResetError:
            break


def server(ip, port):
    server = socket(AF_INET, SOCK_STREAM)
    server.bind((ip, port))
    server.listen(5)

    while True:
        conn, addr = server.accept()
        p = Process(target=talk, args=(conn,))
        p.start()


if __name__ == '__main__':
    server('127.0.0.1', 8080)


