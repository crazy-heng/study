#!/usr/bin/env python
# -*- coding: utf-8 -*-
from multiprocessing import Queue

q = Queue(3)

q.put('hello')
q.put({'a': 1})
q.put([3, 3, 3])
print(q.full())
# q.put(4) #再放就阻塞住了

print(q.get())
print(q.get())
print(q.get())
print(q.empty())  # 空了
# print(q.get()) #再取就阻塞住了
