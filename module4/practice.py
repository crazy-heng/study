#!/usr/bin/env python
# -*- coding:utf-8 -*-
from concurrent.futures import ThreadPoolExecutor
from threading import Thread, Semaphore, Event
import time
import re
import hashlib

sm = Semaphore(10)
event = Event()
pool = ThreadPoolExecutor(5)


def task():
    # with sm:
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
        time.sleep(2)


def password():
    for i in range(3):
        pwd = input('请输入密码:').strip()
        if len(pwd) < 6:
            print("错误密码长度小于6位！")
        elif re.match('^[A-Z]', pwd) == None:
            print('密码必须大写字母开头！')
        else:
            print("yes")
            m = hashlib.md5()
            m.update(pwd.encode(encoding="utf-8"))
            with open('password.txt', 'a') as f:
                f.write(m.hexdigest() + '\n')
            return
    print('超过三次错误！')

# if __name__ == '__main__':
#     print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
#     event.wait(10)
#     for i in range(10):
#         t = Thread(target=task)
#         t.start()


if __name__ == '__main__':
    password()
    for i in range(10):
        pool.submit(task)