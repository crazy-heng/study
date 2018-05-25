#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 1 同步调用，提交后原地拿到执行结果,再执行下一代码，导致串行执行
# from concurrent.futures import ThreadPoolExecutor
# import time
# import random
#
#
# def la(name):
#     print('%s is laing' % name)
#     time.sleep(random.randint(3, 5))
#     res = random.randint(7, 13) * '#'
#     return {'name': name, 'res': res}
#
#
# def weigh(shit):
#     name = shit['name']
#     size = len(shit['res'])
#     print('%s la %s kg' % (name, size))
#
#
# if __name__ == '__main__':
#     pool = ThreadPoolExecutor(13)
#     shit1 = pool.submit(la, 'alex').result()
#     weigh(shit1)
#     shit2 = pool.submit(la, 'peiqi').result()
#     weigh(shit2)
#     shit3 = pool.submit(la, 'yoyo').result()
#     weigh(shit3)

# 2 异步调用，提交完后,不等待任务执行完成
from concurrent.futures import ThreadPoolExecutor
import time
import random


def la(name):
    print('%s is laing' % name)
    time.sleep(random.randint(3, 5))
    res = random.randint(7, 13) * '#'
    return {'name': name, 'res': res}


def weigh(shit):
    shit = shit.result()  # weigh传入对象la，取对象的结果
    name = shit['name']
    size = len(shit['res'])
    print('%s la %s kg' % (name, size))


if __name__ == '__main__':
    pool = ThreadPoolExecutor(13)
    shit1 = pool.submit(la, 'alex').add_done_callback(weigh)
    shit2 = pool.submit(la, 'peiqi').add_done_callback(weigh)
    shit3 = pool.submit(la, 'yoyo').add_done_callback(weigh)
