#!/usr/bin/env python
# -*- coding: utf-8 -*-
import abc

# 同一类事物的多种形态


class Animal(metaclass=abc.ABCMeta):  # 同一类事物:动物
    @abc.abstractmethod
    def talk(self):
        pass


class People(Animal):  # 动物的形态之一:人
    def talk(self):
        print('say hello')


class Dog(Animal):  # 动物的形态之二:狗
    def talk(self):
        print('say wangwang')


class Pig(Animal):  # 动物的形态之三:猪
    def talk(self):
        print('say aoao')


# 多态性指可以不考虑对象类型的情况下直接使用对象
peo1 = People()
peo1.talk()


def func(obj):  # 更进一步,我们可以定义一个统一的接口来使用
    obj.talk()


func(peo1)
