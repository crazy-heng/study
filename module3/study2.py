#!/usr/bin/env python
# -*- coding:utf-8 -*-


# class Mymetaclass(type):
#     def __new__(cls, name, bases, attrs):
#         attrs_new = {}
#         for k, v in attrs.items():
#             if not callable(v) and not k.startswith('__'):
#                 attrs_new[k.upper()] = v
#             else:
#                 attrs_new[k] = v
#         return type.__new__(cls, name, bases, attrs_new)
#
#
# print(type.__new__)
#
#
# class Chinese(metaclass=Mymetaclass):
#     country = 'China'
#     tag = 'Legend of the Dragon'  # 龙的传人
#
#     def walk(self):
#         print('%s is walking' % self.country)
#
#
# print(Chinese.__dict__)


class Mymetaclass(type):
    def __call__(self, *args, **kwargs):
        if args:
            raise TypeError('must key values')
        obj = object.__new__(self)
        for k, v in kwargs.items():
            obj.__dict__[k.upper()] = v
        return obj


class Chinese(metaclass=Mymetaclass):
    country = 'China'
    tag = 'Legend of the Dragon'  # 龙的传人

    def walk(self):
        print('%s is walking' % self.country)


p = Chinese(name='egon', age=18, sex='male')
print(p.__dict__)
