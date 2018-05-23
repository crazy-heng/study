#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from threading import Thread, Event
# import time
#
# event = Event()
#
#
# def student(name):
#     print('学生%s 正在听课' % name)
#     event.wait(1)
#     print('学生%s 课间活动' % name)
#
#
# def teacher(name):
#     print('老师%s 讲课' % name)
#     time.sleep(5)
#     event.set()
#
#
# if __name__ == '__main__':
#     sut1 = Thread(target=student, args=('alex',))
#     sut2 = Thread(target=student, args=('alex1',))
#     sut3 = Thread(target=student, args=('alex2',))
#     tea1 = Thread(target=teacher, args=('tea1',))
#     sut1.start()
#     sut2.start()
#     sut3.start()
#     tea1.start()

from threading import Thread,Event
import threading
import time,random


def conn_mysql():
    count = 1
    while not event.is_set():
        if count > 3:
            return
        print('<%s>第%s次尝试链接' % (threading.current_thread().getName(), count))
        event.wait(0.5)
        count += 1
    print('<%s>链接成功' % threading.current_thread().getName())


def check_mysql():
    print('\033[45m[%s]正在检查mysql\033[0m' % threading.current_thread().getName())
    time.sleep(random.randint(1, 3))
    event.set()


if __name__ == '__main__':
    event = Event()
    conn1 = Thread(target=conn_mysql)
    conn2 = Thread(target=conn_mysql)
    check = Thread(target=check_mysql)

    conn1.start()
    conn2.start()
    check.start()