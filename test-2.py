#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 2-1
# li = ['alex', 'eric', 'rain']
# print("_".join(li))

# 2-2
# li = ["alec", " aric", "Alec", "Tony", "rain"]
#
# tu = ("alec", " aric", "Alex", "Tony", "rain")
#
# dic = {'k1': "alex", 'k2': ' aric', "k3": "Alex", "k4": "Tony"}
#
# for i in li:
#     i = i.strip()
#     if i.startswith("a") or i.startswith("A") and i.endswith("c"):
#         print(i)
# for i in tu:
#     i = i.strip()
#     if i.startswith("a") or i.startswith("A") and i.endswith("c"):
#         print(i)
# for i in dic.values():
#     i = i.strip()
#     if i.startswith("a") or i.startswith("A") and i.endswith("c"):
#         print(i)

# 2-3
# li = ['alex', 'eric', 'rain']
# print(len(li))
# li.append("seven")
# print(li)
# li.insert(0, "tony")
# print(li)
# li[1] = "kelly"
# print(li)
# li.remove("eric")
# print(li)
# pop = li.pop(1)
# print(pop, li)
# li.pop(2)
# print(li)
# for i in range(3):
#     li.pop(1)
# print(li)
# print(li[::-1])
# print(list(reversed(li)))
# for i in range(len(li)):
#     print(i)
# for k, v in enumerate(li, 100):
#     print(k, v)

# 2-4
# li = ["hello", "seven", ["mon", ["h", "kelly"], 'all'], 123, 456]
# print(li[2][1][1])
# print(str.upper(li[2][2]))
# li[2][2] = "ALL"

# 2-5
tu = ('alex', 'eric', 'rain', 'test', 'test1')
print(len(tu))
print(tu[1])
print(tu[2])
print(tu[1:4])
for i in tu:
    print(i)
for i in range(len(tu)):
    print(i)
for k, v in enumerate(tu, 10):
    print(k, v)
