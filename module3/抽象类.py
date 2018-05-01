#!/usr/bin/env python
# -*- coding: utf-8 -*-
import abc  # 利用abc模块实现抽象类


class AllFile(metaclass=abc.ABCMeta):  # 只能被继承不能实例化
    all_type = 'file'

    @abc.abstractmethod  # 定义抽象方法，无需实现功能
    def read(self):
        # '子类必须定义读功能'
        pass

    @abc.abstractmethod  # 定义抽象方法，无需实现功能a
    def write(self):
        # '子类必须定义写功能'
        pass

    # class Txt(All_file):
    #     pass
    #
    # t1=Txt() #报错,子类没有定义抽象方法


class Txt(AllFile):  # 子类继承抽象类，但是必须定义read和write方法
    def read(self):
        print('文本数据的读取方法')

    def write(self):
        print('文本数据的读取方法')