#!/usr/bin/env python
# -*- coding: utf-8 -*-
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import os, random, time


def task(name):
    print('name: %s pid: %s run' % (name, os.getpid()))
    time.sleep(random.randint(1, 3))


if __name__ == '__main__':
    # pool = ProcessPoolExecutor(4)
    pool = ThreadPoolExecutor(5)
    for i in range(10):
        pool.submit(task, 'egon%s' % i)

    pool.shutdown()

    print('主')

