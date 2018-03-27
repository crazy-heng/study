#!/usr/bin/env python
# -*- coding:utf-8 -*-
menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车战':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{},
}

d_choice = menu
last = []
while True:
    for k in d_choice:
        print(k)
    if len(d_choice) > 0:
        choice = input("请选择(q退出，b返回）:").strip()
        if choice in d_choice:
            last.append(d_choice)
            d_choice = d_choice[choice]
        elif choice == "q":
            break
        elif choice == "b" and len(last) == 0:
            # 判断是否在顶层
            print("无法继续返回！")
        elif choice == "b" and len(last) > 0:
            d_choice = eval(str(last[-1]))
            last.pop()
        else:
            print("输入错误！")
    else:
        print("已到最后（q退出，b返回上级）")
        i = input("请选择>>:").strip()
        if i == "q":
            break
        elif i == "b":
            d_choice = eval(str(last[-1]))
            last.pop()
