#!/usr/bin/env python
# -*- coding: utf-8 -*-
from wsgiref.simple_server import make_server


def application(environ, start_response):
    # 按着http协议解析数据:environ
    # 按着http协议组装数据:srart_response
    print(environ)
    print(start_response)
    path = environ.get("PATH_INFO")
    start_response('200 ok', [])

    if path == "/login":
        with open("login.html", "r") as f:
            data = f.read()
    elif path == "/index":
        with open("index.html", "r") as f:
            data = f.read()
    return [data.encode("utf8")]

    # return [b"<h1>hello world</h1>"]

# 封装socket
httped = make_server('', 8080, application)

# 等待用户连接 conn,addr socker.accept()
httped.serve_forever()