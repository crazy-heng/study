#!/usr/bin/env python
# -*- coding:utf-8 -*-
import server

address = '127.0.0.1'
port = 8091


def main():
    try:
        # address = input('输入服务器FTP对外地址：').strip()
        # port = input('输入服务器FTP端口：').strip()
        server.FTPServer((address, int(port))).run()
    except Exception as e:
        print(e)
        print('服务器地址或端口错误！')


if __name__ == '__main__':
    main()
