#!/usr/bin/env python
# -*- coding: utf-8 -*-
from multiprocessing import Process, Queue
import time


def producer(q, name, food):
    for i in range(10):
        res = '%s%s' % (food, i)
        time.sleep(0.5)
        print('%s生产了%s' % (name, res))
        q.put(res)


def consumer(q, name):
    while True:
        res = q.get()
        if res is None:
            break
        time.sleep(1)
        print('%s吃了%s' % (name, res))


if __name__ == '__main__':
    q = Queue()

    p1 = Process(target=producer, args=(q, 'egon', '面包'))
    p2 = Process(target=producer, args=(q, 'egon', '香蕉'))
    c1 = Process(target=consumer, args=(q, 'alex'))
    c2 = Process(target=consumer, args=(q, 'john'))

    p1.start()
    p2.start()
    c1.start()
    c2.start()

    p1.join()
    p2.join()
    q.put(None)
    q.put(None)
    print('主')
