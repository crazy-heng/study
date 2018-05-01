#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 基于元类实现单例模式,比如数据库对象,实例化时参数都一样,就没必要重复产生对象,浪费内存


class Mysql:
    __instance = None

    def __init__(self, host='127.0.0.1', port='3306'):
        self.host = host
        self.port = port

    @classmethod
    def singleton(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = cls(*args, **kwargs)
        return cls.__instance


obj1 = Mysql()
obj2 = Mysql()
print(obj1 is obj2)  # False

obj3 = Mysql.singleton()
obj4 = Mysql.singleton()
print(obj3 is obj4)  # True

# 元类方式


class Mymeta(type):
    def __init__(self, class_name, class_bases, class_dic):
        if not class_name.istitle():
            raise TypeError('类名首字母必须大写')
        if '__doc__' not in class_dic or not class_dic['__doc__'].strip():
            raise TypeError('必须有注释，且不为空！')
        super(Mymeta, self).__init__(class_name, class_bases, class_dic)
        self.__instance = None

    def __call__(self, *args, **kwargs):  # 用call控制实例化
        if not self.__instance:
            # 造一个空对象
            obj = object.__new__(self)
            # 初始化obj
            self.__init__(obj, *args, **kwargs)
            self.__instance = obj
        # 返回obj
        return obj


class Mysql(object, metaclass=Mymeta):
    def __init__(self, host='127.0.0.1', port='3306'):
        self.host = host
        self.port = port
