#!/usr/bin/env python
# -*- coding: utf-8 -*-
from threading import Thread, current_thread, active_count, enumerate
import time


def task():
    print('%s is running' % current_thread().getName())
    time.sleep(2)
    print('%s is done' % current_thread().getName())


if __name__ == '__main__':
    t = Thread(target=task, name='子线程')
    t.start()
    # t.setName('儿子线程1')
    # t.join()
    # print(t.is_alive())

    # print(active_count())
    # print(enumerate())
    print('主线程', current_thread().getName())
