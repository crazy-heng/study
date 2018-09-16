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
    with open("templates/favicom.ico", 'rb') as f:
        data = f.read()
    return data


def timer(environ):
    import datetime

    now = datetime.datetime.now().strftime("%y-%m-%d %X")
    return now.encode("utf8")
