#!/usr/bin/env python
# -*- coding: utf-8 -*-
from multiprocessing import Process
import time,os


def task(name):
    print('%s is running,parent id is %s' % (os.getpid(), os.getppid()))
    time.sleep(3)
    print('%s is done,parent id is %s' % (os.getpid(), os.getppid()))


if __name__ == '__main__':
    p = Process(target=task, args=('子进程1',))
    p.start()  # 仅仅只是发送一个信号

    print('主', os.getpid(), os.getppid())
