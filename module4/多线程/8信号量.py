#!/usr/bin/env python
# -*- coding: utf-8 -*-
from threading import Thread, Semaphore, Event
import threading
import time, random

sm = Semaphore(5)
event = Event()


def task():
    with sm:
        print('%s in' % threading.currentThread().getName())
        time.sleep(random.randint(1, 3))


if __name__ == '__main__':
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
    event.wait(10)
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
    for i in range(10):
        t = Thread(target=task)
        t.start()