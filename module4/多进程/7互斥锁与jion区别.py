#!/usr/bin/env python
# -*- coding: utf-8 -*-
from multiprocessing import Process, Lock
import time, json


def search(name):
    dic = json.load(open('db.txt'))
    time.sleep(1)
    print('\033[45m%s 查到剩余票数%s\033[0m' % (name, dic['count']))


def get(name):
    dic = json.load(open('db.txt'))
    time.sleep(1)  # 模拟读数据的网络延迟
    if dic['count'] > 0:
        dic['count'] -= 1
        time.sleep(1)  # 模拟写数据的网络延迟
        json.dump(dic, open('db.txt', 'w'))
        print('\033[46m%s 购票成功\033[0m' % name)
    else:
        print('购票失败')


def task(name):
    search(name)
    # mutex.acquire()
    get(name)
    # mutex.release()


if __name__ == '__main__':
    # mutex = Lock()
    for i in range(10):  # 模拟并发10个客户端抢票
        name = '<路人%s>' % i
        p = Process(target=task, args=(name,))
        p.start()
        p.join()  # 代码整体锁定
