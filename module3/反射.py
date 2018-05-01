#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 反射：通过字符串映射到对象的属性


class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print('%s is talking' % self.name)


obj = People('egon', 18)
print(hasattr(obj, 'name'))  # 判断obj里有没有name字典key，也可判断类
print(getattr(obj, 'name', None))  # 获取值没有则返回None
print(getattr(obj, 'sex', None))
setattr(obj, 'name', 'EGON')
print(getattr(obj, 'name', None))
# delattr(obj, 'sex')


class Service:
    def run(self):
        while True:
            inp = input('>>').strip()
            cmds = inp.split()
            if hasattr(self, cmds[0]):
                func = getattr(self, cmds[0])
                func(cmds)

    def get(self, cmds):
        print('get ...', cmds)

    def put(self, cmds):
        print('put ...', cmds)


obj = Service()
obj.run()
