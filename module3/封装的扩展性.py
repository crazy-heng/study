#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 类的设计者


class Room:
    def __init__(self, name, owner, width, length, high):
        self.name = name
        self.owner = owner
        self.__width = width
        self.__length = length
        self.__high = high

    def tell_area(self):  # 对外提供的接口，隐藏了内部的实现细节，此时我们想求的是面积
        return self.__width * self.__length


# 使用者
r1 = Room('卧室', 'egon', 20, 20, 20)
print(r1.tell_area())  # 使用者调用接口tell_area
