#!/usr/bin/env python
# -*- coding: utf-8 -*-
from threading import Thread
import time


# def task(name):
#     print('%s is running' % name)
#     time.sleep(1)
#     print('%s is done' % name)
#
#
# if __name__ == '__main__':
#     t = Thread(target=task, args=('子线程1',))
#     t.start()  # 仅仅只是发送一个信号
#
#     print('主')


class MyThread(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print('%s is running' % self.name)
        time.sleep(1)
        print('%s is done' % self.name)


if __name__ == '__main__':
    t = MyThread('子线程1')
    t.start()

    print('主')