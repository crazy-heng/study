#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 死锁
# from threading import Thread, Lock
# import time
#
# mutexA = Lock()
# mutexB = Lock()
#
#
# class MyThread(Thread):
#     def run(self):
#         self.f1()
#         self.f2()
#
#     def f1(self):
#         mutexA.acquire()
#         print('%s 拿到了A锁' % self.name)
#
#         mutexB.acquire()
#         print('%s 拿到了B锁' % self.name)
#         mutexB.release()
#         mutexA.release()
#
#     def f2(self):
#         mutexB.acquire()
#         print('%s 拿到了B锁' % self.name)
#         time.sleep(0.1)
#         mutexA.acquire()
#         print('%s 拿到了A锁' % self.name)
#         mutexA.release()
#         mutexB.release()
#
#
# if __name__ == '__main__':
#     for i in range(10):
#         t = MyThread()
#         t.start()

# 互斥锁只能acquire一次
# mutexA = Lock()
# mutexA.acquire
# mutexA.release
# 递归锁:可以连续acquire多次，每一次acquire计数器加1，只有计数为0，才能被抢到
from threading import Thread, RLock
import time

mutexA = mutexB = RLock()


class MyThread(Thread):
    def run(self):
        self.f1()
        self.f2()

    def f1(self):
        mutexA.acquire()
        print('%s 拿到了A锁' % self.name)

        mutexB.acquire()
        print('%s 拿到了B锁' % self.name)
        mutexB.release()
        mutexA.release()

    def f2(self):
        mutexB.acquire()
        print('%s 拿到了B锁' % self.name)
        time.sleep(1)
        mutexA.acquire()
        print('%s 拿到了A锁' % self.name)
        mutexA.release()
        mutexB.release()


if __name__ == '__main__':
    for i in range(10):
        t = MyThread()
        t.start()
