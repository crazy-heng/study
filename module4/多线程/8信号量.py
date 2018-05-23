#!/usr/bin/env python
# -*- coding: utf-8 -*-
from threading import Thread, Semaphore
import threading
import time, random

sm = Semaphore(5)


def task():
    with sm:
        print('%s in' % threading.currentThread().getName())
        time.sleep(random.randint(1, 3))


if __name__ == '__main__':
    for i in range(10):
        t = Thread(target=task)
        t.start()