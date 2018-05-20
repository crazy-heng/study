#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from multiprocessing import Process
# import time,os
#
#
# def task(name):
#     print('%s is running,parent id is %s' % (os.getpid(), os.getppid()))
#     time.sleep(3)
#     print('%s is done,parent id is %s' % (os.getpid(), os.getppid()))
#
#
# if __name__ == '__main__':
#     p = Process(target=task, args=('子进程1',))
#     p.start()  # 仅仅只是发送一个信号
#
#     p.join()  # 等待子进程结束
#     print('主', os.getpid(), os.getppid())
#

from multiprocessing import Process
import time,os


def task(name, n):
    print('%s is running,parent id is %s' % (name, os.getppid()))
    time.sleep(n)


if __name__ == '__main__':
    p1 = Process(target=task, args=('子进程1', 1))
    p2 = Process(target=task, args=('子进程2', 2))
    p3 = Process(target=task, args=('子进程3', 3))
    p1.start()  # 仅仅只是发送一个信号
    p2.start()
    p3.start()
    p1.terminate()
    # time.sleep(2)
    print(p1.is_alive())
    p1.join()
    p2.join()
    p3.join()
    print(p1.is_alive())
    print('主', os.getpid(), os.getppid())
