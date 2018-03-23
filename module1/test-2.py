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
# tu = ('alex', 'eric', 'rain', 'test', 'test1')
# print(len(tu))
# print(tu[1])
# print(tu[2])
# print(tu[1:4])
# for i in tu:
#     print(i)
# for i in range(len(tu)):
#     print(i)
# for k, v in enumerate(tu, 10):
#     print(k, v)

# 2-6
# tu = ("alex", [11, 22, {"k1": 'v1', "k2": ["age", "name"], "k3": (11, 22, 33)}, 44])
# tu[1][2]["k2"].append("seven")
# print(tu)

# 2-7
# dic = {'k1': "v1", "k2": "v2", "k3": [11, 22, 33]}
# print(dic.keys())
# print(dic.values())
# print(dic.items())
# dic["k4"] = "v4"
# print(dic)
# dic["k1"] = "alex"
# print(dic)
# dic["k3"].append(int(44))
# print(dic)
# dic["k3"].insert(1, int(18))
# print(dic)
#
# # 2-8
# s = "alex"
# li = ["alex", "seven"]
# tu = ('Alex', "seven")
# print(list(s))
# print(tuple(s))
# print(tuple(li))
# print(list(tu))
# print(dict(zip([i for i in range(10, len(li) + 10)], li)))

# 2-9
# li = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
# dic = {"k1": [], "k2": []}
# for i in li:
#     if int(i) <= 66:
#         dic["k1"].append(i)
#     else:
#         dic["k2"].append(i)
# print(dic)

# 2-10
# li = ["手机", "电脑", '鼠标垫', '游艇']
# for index, v in enumerate(li, 1):
#     print(index, v)
# i = input("请输入选择：")
# print(li[int(i)-1])

# 2-13
# l1 = {11, 22, 33}
# l2 = {22, 33, 44}
# print(l1 & l2)
# print(l1 | l2)
# print(l1 - l2)
# print(l2 - l1)
# print(l1 ^ l2)

# 2-14
# for i in range(1, 101):
#     print(i)
# s = 100
# for i in range(0, 100):
#     print(s)
#     s -= 1
# i = 1
# while i <= 100:
#     print(i)
#     i += 1
# i = 100
# while i > 0:
#     print(i)
#     i -= 1

# 2-15
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print("%s*%s=%2s" % (j, i, i*j), end=" ")
#     print('')
# print('\n'.join([' '.join(["%d*%d=%2s" % (y, x, x*y) for y in range(1, x+1)]) for x in range(1, 10)]))

# 2-17
li = [1, 3, 78, 96, 68, 2, 41, 24, 4, 85, 5]
k = 0
test = None
while len(li) - k > 1:
    i = 0
    if str(li) == test:
        break
    test = str(li)
    while len(li) - i > 1:
        if li[i+1] < li[i]:
            j = li[i]
            li[i] = li[i+1]
            li[i+1] = j
        i += 1
    k += 1
    print(li)
print(sorted(li))
