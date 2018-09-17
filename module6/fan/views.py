#!/usr/bin/env python
# -*- coding: utf-8 -*-


def login(environ):
    with open("templates/login.html", 'rb') as f:
        data = f.read()
    return data


def index(environ):
    with open("templates/index.html", 'rb') as f:
        data = f.read()
    return data


def fav(environ):
    with open("templates/favicon.ico", 'rb') as f:
        data = f.read()
    return data


def timer(environ):
    import datetime

    now = datetime.datetime.now().strftime("%y-%m-%d %X")
    return now.encode("utf8")


def auth(request):
    from urllib.parse import parse_qs

    try:
        request_body_size = int(request.get('CONTENT_LENGTH', 0))
    except (ValueError):
        request_body_size = 0
        # 当请求方式是POST时, 变量将会被放在存在域wsgi.input文件中的HTTP请求信息中, 由WSGI 服务器一起发送.
    request_body = request['wsgi.input'].read(request_body_size)
    d = parse_qs(request_body)

    print(d.get(b"user"))
    user = d.get(b"user")[0].decode("utf8")
    pwd = d.get(b"pwd")[0].decode("utf8")

    import pymysql

    conn = pymysql.connect(
        host='47.91.207.76',
        port=3306,
        user='wordpress',
        password='word',
        db='homework',
        charset='utf8')
    cur = conn.cursor()
    sql = "select * from userinfo where NAME ='%s' and PASSWORD = '%s'" % (user, pwd)
    cur.execute(sql)

    if cur.fetchone():
        f = open("templates/backend.html", "rb")

        data = f.read()
        return data

    else:
        return b"user or pwd is wrong"
