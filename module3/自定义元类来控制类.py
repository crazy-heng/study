#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Mymeta(type):
    def __init__(self, class_name, class_bases, class_dic):
        if not class_name.istitle():
            raise TypeError('类名首字母必须大写')
        if '__doc__' not in class_dic or not class_dic['__doc__'].strip():
            raise TypeError('必须有注释，且不为空！')
        super(Mymeta, self).__init__(class_name, class_bases, class_dic)

    def __call__(self, *args, **kwargs):  # 用call控制实例化
        print(self)
        print(args)
        # 造一个空对象
        obj = object.__new__(self)
        # 初始化obj
        self.__init__(obj, *args, **kwargs)
        # 返回obj
        return obj


class Chinese(object, metaclass=Mymeta):
    '''
    注释
    '''
    country = 'China'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print('%s is talking' % self.name)


Chinese('egon', 18)
