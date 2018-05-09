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
    m = hashlib.md5()
    m.update(file)
    return m.hexdigest()