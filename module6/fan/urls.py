#!/usr/bin/env python
# -*- coding: utf-8 -*-
from views import *

url_patterns = [
    ("/login", login),
    ("/index", index),
    ("/favicon.ico", fav),
    ("/time", timer)
]
