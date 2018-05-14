#!/usr/bin/env python
# -*- coding:utf-8 -*-
import server
import setting


def main():
    try:
        # address = input('输入服务器FTP对外地址：').strip()
        # port = input('输入服务器FTP端口：').strip()
        server.FTPServer((setting.address, int(setting.port))).run()
    except Exception as e:
        print(e)
        print('服务器地址或端口错误！')


if __name__ == '__main__':
    main()
