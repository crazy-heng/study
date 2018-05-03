#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from core import rw


userinfo = BASE_DIR + '/db/userinfo'
teacher = BASE_DIR + '/db/teacher/'
student = BASE_DIR + '/db/student/'
course = BASE_DIR + '/db/course/'
classes = BASE_DIR + '/db/classes/'

user_dic = rw.read(userinfo)
# user_dic["classes"].pop()
# # del user_dic['fan']
# rw.write(student + 's1', user_dic)