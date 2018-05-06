#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import subprocess
import struct
import json
import os

share_dir = r'E:\python\study\module3\socket测试\文件传输\server'

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
phone.bind(('127.0.0.1', 9002))  # 0-65535 0-1024系统用
phone.listen(5)

print('starting')
while True:  # 链接循环不断提供服务
    conn, client_addr = phone.accept()
    print(client_addr)

    while True:
        try:
            # 1 接收命令
            res = conn.recv(8096)  # get a.txt
            if not res:  # linux收不到会死循环
                break
            print('客户端数据', res)

            # 2 解析命令，提取相应命令参数
            cmds = res.decode('utf-8').split()
            filename = cmds[1]
            # 3 以读的方式打开文件，以bytes形式

            # 第一步：制作报头,struct模块用i格式固定长度是4
            header_dic = {
                'file_name': filename,
                'md5': 'xxxeddexxx',
                'file_size': os.path.getsize('%s/%s' % (share_dir, filename))
            }
            header_json = json.dumps(header_dic)
            header_bytes = header_json.encode('utf-8')

            # 第二步 发送报头长度
            header = struct.pack('i', len(header_bytes))
            conn.send(header)
            # 第三步：把报头数据发送给客户端
            conn.send(header_bytes)

            # 第四步：再发送真实数据
            with open('%s/%s' % (share_dir, filename), 'rb') as f:
                for line in f:
                    conn.send(line)

        except ConnectionResetError:  # windows系统用try处理客户端断开报错退出
            break
    conn.close()

phone.close()
