#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import struct
import json

share_dir = r'E:\python\study\module3\socket测试\文件传输\client'
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.connect(('127.0.0.1', 9002))

while True:
    # 1 发命令
    cmd = input('-->').strip()
    if not cmd:
        continue
    phone.send(cmd.encode('utf-8'))

    # 2 接收文件内容，以写的方式打开文件，接受服务端发来的文件写入新文件

    # 第一步：先收报头长度
    header = phone.recv(4)
    header_size = struct.unpack('i', header)[0]
    # 第二步：收报头数据
    header_bytes = phone.recv(header_size)

    # 第三步：取报头信息
    header_json = header_bytes.decode('utf-8')
    header_dic = json.loads(header_json)
    total_size = header_dic['file_size']
    file_name = header_dic['file_name']

    # 第四步：接收真实的数据
    with open('%s/%s' % (share_dir, file_name), 'wb') as f:
        recv_size = 0
        while recv_size < total_size:
            line = phone.recv(1024)  # 1024一个坑
            f.write(line)
            recv_size += len(line)
            print('总大小%s,已下载%s' % (total_size, recv_size))

phone.close()
