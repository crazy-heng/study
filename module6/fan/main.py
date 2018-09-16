#!/usr/bin/env python
# -*- coding: utf-8 -*-
from wsgiref.simple_server import make_server
from urls import url_patterns


def application(environ, start_response):
    print("path", environ.get("PATH_INFO"))
    start_response('200 ok', [])

    path = environ.get("PATH_INFO")

    # 方案一
    # if path == "/favicon.ico":
    #     with open("favicon.ico", "rb") as f:
    #         data = f.read()
    #     return [data]
    # elif path == "/login":
    #     with open("login.html", 'rb') as f:
    #         data = f.read()
    #     return [data]
    # elif path == "/index":
    #     with open("index.html", 'rb') as f:
    #         data = f.read()
    #     return [data]

    func = None
    for item in url_patterns:
        if path == item[0]:
            func = item[1]
            break

    if func:
        return [func(environ)]
    else:
        return [b"404!"]


# 封装socket
httped = make_server('', 8088, application)

# 等待用户连接 conn,addr socker.accept()
httped.serve_forever()