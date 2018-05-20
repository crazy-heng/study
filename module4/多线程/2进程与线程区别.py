#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 1 进程开销远大于线程
# from threading import Thread
# from multiprocessing import Process
# import time
#
#
# def task(name):
#     print('%s is running' % name)
#     time.sleep(1)
#     print('%s is done' % name)
#
#
# if __name__ == '__main__':
#     # p = Process(target=task, args=('子进程1',))
#     # p.start()
#
#     t = Thread(target=task, args=('子线程1',))
#     t.start()
#
#     print('主')

# 2 同一进程内的多个线程共享进程的地址空间
# from threading import Thread
# from multiprocessing import Process
#
# n = 100
#
#
# def task():
#     global n
#     n = 0
#
#
# if __name__ == '__main__':
#     # p = Process(target=task,)
#     # p.start()
#     # p.join()  # n = 100
#
#     t = Thread(target=task, )
#     t.start()
#     t.join()  # n = 0
#
#     print('主', n)

#  3 看一眼pid
from threading import Thread
from multiprocessing import Process
import os


def task():
    print(os.getpid(), os.getppid())


if __name__ == '__main__':
    p = Process(target=task,)
    p.start()

    t = Thread(target=task, )
    t.start()

    print('主进程', os.getpid())