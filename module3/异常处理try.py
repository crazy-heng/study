#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 多分支：被监测的代码抛出异常有多种可能性，并且我们需要针对每种异常类型都定制专门的处理逻辑
# try:
#     print('--->1')
#     name
#     print('---->2')
#     l = [1, 2, 3]
#     l[100]
#     print('---->3')
#     d = {}
#     d['name']
#     print('---->4')
# except NameError as e:
#     print('--->', e)
# except IndexError as e:
#     print('--->', e)
# except KeyError as e:
#     print('--->', e)

# 万能异常：Exception,被检测代码有多种可能性，并且针对所有一场类型都只用一种处理逻辑
# try:
#     print('---->1')
#     # name
#     print('---->2')
#     l = [1, 2, 3]
#     l[100]
#     print('---->3')
#     d = {}
#     d['name']
#     print('---->4')
# except Exception as e:
#     print('--->', e)
#
# print('end')

# 其他结构
# try:
#     print('---->1')
#     # name
#     print('---->2')
#     l = [1, 2, 3]
#     # l[100]
#     print('---->3')
#     d = {}
#     d['name']
#     print('---->4')
# except NameError as e:
#     print('--->', e)
# except IndexError as e:
#     print('--->', e)
# except KeyError as e:
#     print('--->', e)
# except Exception as e:
#     print('--->', e)
# else:
#     print('被检测代码块没有发生异常')
#
# finally:
#     print('不管有没有异常都会执行')
# print('end')

# 主动异常 raise： 异常对象
# class People:
#     def __init__(self, name, age):
#         if not isinstance(name, str):
#             raise TypeError('名字必须是str类型')
#         self.name = name
#         self.age = age
#
#
# p = People(333, 18)

# 自定义异常类型
class Myexception(BaseException):
    def __init__(self, msg):
        super(Myexception, self).__init__()
        self.msg = msg

    def __str__(self):
        return '</%s>' % self.msg

raise Myexception('我的异常类型') # print obj

# 断言assert
# info = {}
# info['name'] = 'egon'
# # info['age'] = 18
#
# assert ('name' in info) and ('age' in info)
#
# if info['name'] == 'egon' and info['age'] > 10:
#     print('welcome')
