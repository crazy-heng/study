#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import struct
import json

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.connect(('127.0.0.1', 9001))

while True:
    # 1 发命令
    cmd = input('-->').strip()
    if not cmd:
        continue
    phone.send(cmd.encode('utf-8'))

    # 2 拿命令结果
    # 第一步：先收报头长度
    header = phone.recv(4)
    header_size = struct.unpack('i', header)[0]
    # 第二步：收报头数据
    header_bytes = phone.recv(header_size)

    # 第三步：取报头信息
    header_json = header_bytes.decode('utf-8')
    header_dic = json.loads(header_json)
    total_size = header_dic['total_size']

    # 第四步：接收真实的数据
    recv_size = 0
    recv_data = b''
    while recv_size < total_size:
        res = phone.recv(1024)  # 1024一个坑
        recv_data += res
        recv_size += len(res)
    print(recv_data.decode('gbk'))  # linux用utf-8解码，windows用gbk解码

phone.close()
