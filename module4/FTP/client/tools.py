#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
import hashlib


def read(name):
    with open(name, 'r') as f:
        data = (json.load(f))
        return data


def write(name, data):
    with open(name, 'w') as f:
        json.dump(data, f)


def md5(file):
    with open(file, 'rb') as f:
        m = hashlib.md5()
        m.update(f.read())
        return m.hexdigest()


def md5_user(file):
        m = hashlib.md5()
        m.update(file)
        return m.hexdigest()