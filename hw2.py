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

D = menu

# while D:
city = list(D.keys())
# i = len(city)
# print(city,i)
# print(D['上海'])
end_flag = 0

while True:
    print(city)
    ch_city = input("请选择城市：(按q退出）")
    if ch_city == 'q':exit()
    # elif len(D[ch_city]) == 0:break
    elif ch_city in city:
        print(u"已选择{0:s}".format(ch_city))
        while len(D[ch_city]) != 0:
            D_qu = D[ch_city]
            qu = list(D_qu.keys())
            print(qu)
            ch_qu = input("请选择区域：(按0返回、按q退出）")
            if ch_qu == '0':
                break
            elif ch_qu in qu:
                print(u"已选择{0:s}区域{1:s}".format(ch_city, ch_qu))

                while len(D[ch_city][ch_qu]) != 0:
                    D_street = D[ch_city][ch_qu]
                    street = list(D_street.keys())
                    print(street)
                    ch_street = input("请选择地块：(按0返回、按q退出）")
                    if ch_street == '0':
                        break
                    elif ch_street in street:
                        print(u"已选择{0:s}{1:s}地块{2:s}".format(ch_city, ch_qu, ch_street))

                        while len(D[ch_city][ch_qu][ch_street]) != 0:
                            D_company = D[ch_city][ch_qu][ch_street]
                            company = list(D_company.keys())
                            print(company)
                            ch_company = input("请选择公司：(按0返回、按q退出）")
                            if ch_company == '0':
                                break
                            elif ch_company in company:
                                print(u"已选择{0:s}{1:s}{2:s}公司{3:s}".format(ch_city, ch_qu, ch_street, ch_company))
                                exit()
                            elif ch_company == 'q':
                                exit()
                            else:
                                print("输入错误请重新输入公司")

                    elif ch_street == 'q':
                        exit()
                    else:
                        print("输入错误请重新输入区")


            elif ch_city == 'q':
                exit()
            else:
                print("输入错误请重新输区域")

    else:
        print("输入错误请重新输入城市")
#print("您已选择%s"%ch_city)





