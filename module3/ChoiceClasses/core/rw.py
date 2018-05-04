#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pickle
import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


def read(name):
    with open(name, 'rb') as f:
        data = (pickle.load(f))
        return data


def write(name, data):
    with open(name, 'wb') as f:
        pickle.dump(data, f)
