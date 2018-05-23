#!/usr/bin/env python
# -*- coding: utf-8 -*-
import queue

# q = queue.Queue(3)
#
# q.put('first')
# q.put(2)
# q.put('third')
# # q.put(4, block=True, timeout=3)
#
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get(block=False))

# 先进后出
q = queue.LifoQueue(3)
q.put('first')
q.put(2)
q.put('third')

print(q.get())
print(q.get())
print(q.get())

# 优先级
q = queue.PriorityQueue(3)

q.put((10, 'one'))
q.put((20, 'three'))
q.put((15, 'two'))

print(q.get())
print(q.get())
print(q.get())