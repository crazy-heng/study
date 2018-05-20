#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from threading import Thread, current_thread, active_count, enumerate
# import time
#
#
# def sayhi(name):
#     time.sleep(1)
#     print('%s say hello' % name)
#
#
# if __name__ == '__main__':
#     t = Thread(target=sayhi, args=('egon',))
#     t.daemon = True
#     t.start()
#
#     print('主线程')
#     print(t.is_alive())

from threading import Thread
import time


def foo():
    print(123)
    time.sleep(1)
    print("end123")
    time.sleep(3)
    print("end no see")  # 时间大于线程，不会被打印


def bar():
    print(456)
    time.sleep(3)
    print("end456")


if __name__ == '__main__':
    t1 = Thread(target=foo)
    t2 = Thread(target=bar)

    t1.daemon = True  # 守护线程时间段能运行完
    t1.start()
    t2.start()  # 3秒后主线程随t2线程关闭，守护线程也关闭
    print("main-------")