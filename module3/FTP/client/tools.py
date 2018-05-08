#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json


def read(name):
    with open(name, 'r') as f:
        data = (json.load(f))
        return data


def write(name, data):
    with open(name, 'w') as f:
        json.dump(data, f)
