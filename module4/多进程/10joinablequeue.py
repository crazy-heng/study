#!/usr/bin/env python
# -*- coding: utf-8 -*-
from multiprocessing import Process, Queue, JoinableQueue
import time


def producer(q, name, food):
    for i in range(5):
        res = '%s%s' % (food, i)
        time.sleep(0.5)
        print('%s生产了%s' % (name, res))
        q.put(res)
    q.join()


def consumer(q, name):
    while True:
        res = q.get()
        if res is None:
            break
        time.sleep(1)
        print('%s吃了%s' % (name, res))
        q.task_done()


if __name__ == '__main__':
    q = JoinableQueue()

    p1 = Process(target=producer, args=(q, 'egon', '面包'))
    p2 = Process(target=producer, args=(q, 'egon', '香蕉'))
    c1 = Process(target=consumer, args=(q, 'alex'))
    c2 = Process(target=consumer, args=(q, 'john'))
    c3 = Process(target=consumer, args=(q, 'peter'))
    c1.daemon = True
    c2.daemon = True
    c3.daemon = True

    p1.start()
    p2.start()
    c1.start()
    c2.start()
    c3.start()

    p1.join()
    p2.join()
    print('主')