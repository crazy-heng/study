#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 读取账号信息导入成字典
accounts = {}
f = open("users.txt", 'r+', encoding="utf-8")
for line in f.readlines():
    line = line.strip().split(",")
    accounts[line[0]] = line
print(accounts)


# 写回文件函数
def save_file(account_dic):
    f.seek(0)
    f.truncate()
    for k in account_dic:
        row = ",".join(account_dic[k])
        f.write("%s\n" % row)
    f.flush()


# where条件函数返回列索引
def where(account_dic, content):
    if content in account_dic["staff_id"]:
        return account_dic["staff_id"].index(content)
    else:
        return False


# find查找函数
def find_accounts(account_dic, fd1, fd2, fd3, fd4):
    i = 0
    li = ["<", ">", ">=", "<="]
    if fd1 == "*":
        if where(accounts, fd2):
            num = where(accounts, fd2)
            for v in account_dic:
                if v == "staff_id":
                    pass
                elif fd3 in li and eval(account_dic[v][num]+fd3+fd4):
                    print(account_dic[v])
                    i += 1
                elif fd3 == "=" and fd4 in account_dic[v][num] == fd4:
                    print(account_dic[v])
                    i += 1
                elif fd3 == "like" and fd4 in account_dic[v][num]:
                    print(account_dic[v])
                    i += 1
            print("无符合条件数据！") if i == 0 else print("查找到%s条数据" % i)
        else:
            print("没有[%s]这个字段！" % fd2)
    elif set(fd1.split(",")) < set(account_dic["staff_id"]):
        if where(accounts, fd2):
            num = where(accounts, fd2)
            for v in account_dic:

                # 显示指定列函数
                def p_list(dic, _li):
                    if len(_li) == 1:
                        print(dic[v][where(dic, _li[0])])
                    elif len(_li) == 2:
                        print(dic[v][where(dic, _li[0])] + " " +
                              dic[v][where(dic, _li[1])])
                    elif len(_li) > 2:
                        print("字段数过多，只能2个！")

                if v == "staff_id":
                    pass
                elif fd3 in li and eval(account_dic[v][num]+fd3+fd4):
                    p_list(account_dic, fd1.split(","))
                    i += 1
                elif fd3 == "=" and fd4 in account_dic[v][num] == fd4:
                    p_list(account_dic, fd1.split(","))
                    i += 1
                elif fd3 == "like" and fd4 in account_dic[v][num]:
                    p_list(account_dic, fd1.split(","))
                    i += 1
            print("无符合条件数据！") if i == 0 else print("查找到%s条数据" % i)
    else:
        print("[%s]字段错误" % fd1)


# add新增函数
def add_accounts(account_dic, _add):
    if len(_add) == 5:
        for v in account_dic:
            if _add[2] == account_dic[v][3]:
                exit("电话号不能重复！")
        a = []
        i = list(account_dic.keys())
        i.remove("staff_id")
        for k in i:
            a.append(int(k))
        num = max(a) + 1
        _add = [str(num)] + _add
        account_dic[str(num)] = _add
        save_file(account_dic)


# del删除函数
def del_accounts(account_dic, _num):
    a = _num.split("=")
    if len(a) == 2 and a[0] == "id" and a[1].isdigit():
        account_dic.pop(a[1])
        save_file(account_dic)
    else:
        print("删除条件错误%s" % _num)


# update修改函数
def update_accounts(account_dic, up1, up2, up3, up4):
    i = 0
    if len(up1.split("=")) == 2 and up1.split("=")[0] in account_dic["staff_id"]:
        key = where(accounts, up1.split("=")[0])
        if where(accounts, up2):
            num = where(accounts, up2)
            if up3 != "=":
                exit("参数%s %s %s错误" % (up2, up3, up4))
            for v in account_dic:
                if account_dic[v][num] == up4:
                    account_dic[v][key] = up1.split("=")[1].strip('"')
                    print(account_dic[v])
                    i += 1
            save_file(account_dic)
            print("无符合条件数据！") if i == 0 else print("修改%s条数据" % i)
        else:
            print("参数[%s %s %s]错误" % (up2, up3, up4))
    else:
        print("条件[%s]错误！" % up1)


# 运行函数
def main():
    # 拆分命令为几个参数
    _cmd = input("请输入命令：")
    if _cmd.startswith("find "):
        li = _cmd.split(" ")
        if len(li) == 8:
            _find1, _find2, _find3, _find4 = li[1], li[5], li[6], li[7].strip('"')
            print("执行查找。。。")
            find_accounts(accounts, _find1, _find2, _find3, _find4)
        else:
            print("命令参数有误！")
    elif _cmd.startswith("add "):
        li = _cmd.split("table ")
        if len(li) == 2:
            _add = li[1]
            print("执行添加。。。")
            add_accounts(accounts, _add.split(","))
        else:
            print("命令参数有误！")
    elif _cmd.startswith("del "):
        li = _cmd.split(" ")
        if len(li) == 5:
            _del = li[4]
            print("执行删除。。。")
            del_accounts(accounts, _del)
        else:
            print("命令参数有误！")
    elif _cmd.startswith("UPDATE "):
        li = _cmd.split(" ")
        if len(li) == 8:
            _up1, _up2, _up3, _up4 = li[3], li[5], li[6], li[7].strip('"')
            print("执行修改。。。")
            update_accounts(accounts, _up1, _up2, _up3, _up4)
        else:
            print("命令参数有误！")
    else:
        print("命令输入有误！")


if __name__ == "__main__":
    main()