#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import struct
import json
import os
import tools

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class FTPClient:
    address_type = socket.AF_INET
    socket_type = socket.SOCK_STREAM
    allow_reuse_address = False
    max_packet_size = 8192
    coding = 'utf-8'
    request_queue_size = 5
    client_dir = BASE_DIR + '/download'

    def __init__(self, server_address, user_name, user_info, connect=True):
        self.server_address = server_address
        self.user_name = user_name
        self.user_info = user_info
        self.socket = socket.socket(self.address_type, self.socket_type)
        self.user_dir = user_name
        if connect:
            try:
                self.client_connect()
            except Exception:
                self.client_close()
                raise

    def client_connect(self):
        self.socket.connect(self.server_address)

    def client_close(self):
        self.socket.close()

    def run(self):
        while True:
            # 1 发命令
            cmds = input('-->').strip()
            if not cmds:
                continue
            self.socket.send(('%s %s' % (self.user_dir, cmds)).encode('utf-8'))
            cmd = cmds.split()
            if cmd[0] == 'get':
                self.get(cmd)
            elif cmd[0] == 'put':
                self.put(cmd)
            elif cmd[0] == 'dir':
                self.show(cmd)
            elif cmd[0] == 'cd':
                self.cd(cmd)
                # self.socket.send(('%s %s' % (self.user_dir, cmds)).encode('utf-8'))
                # self.show(cmd)

            print('当前所在目录%s' % self.user_dir)
        # self.client_close()

    def put(self, cmds):
        cmd = cmds[0]
        filename = cmds[1]
        if not os.path.isfile('%s/%s' % (self.client_dir, filename)):
            print('file:%s/%s is not exists' % (self.client_dir, filename))
            return
        else:
            filesize = os.path.getsize('%s/%s' % (self.client_dir, filename))
        # 判断上传文件是否超过剩余配额
        if filesize > self.user_info[self.user_name][2]:
            print('已超配额无法上传%s！当前剩余配额%s！' % (filesize, self.user_info[self.user_name][2]))
            return

        head_dic = {'cmd': cmd, 'user_name': self.user_name, 'file_name': filename, 'file_size': filesize}
        print(head_dic)
        head_json = json.dumps(head_dic)
        head_json_bytes = bytes(head_json, encoding=self.coding)

        head_struct = struct.pack('i', len(head_json_bytes))
        self.socket.send(head_struct)
        self.socket.send(head_json_bytes)
        send_size = 0
        with open('%s/%s' % (self.client_dir, filename), 'rb') as f:
            for line in f:
                self.socket.send(line)
                send_size += len(line)
                print(send_size)
            else:
                print('upload successful')
                self.user_info[self.user_name][2] -= send_size
                tools.write('userlist', self.user_info)

    def get(self, cmds):
        header = self.socket.recv(4)
        header_size = struct.unpack('i', header)[0]
        # 第二步：收报头数据
        header_bytes = self.socket.recv(header_size)

        # 第三步：取报头信息
        header_json = header_bytes.decode('utf-8')
        header_dic = json.loads(header_json)
        total_size = header_dic['file_size']
        file_name = header_dic['file_name']

        # 第四步：接收真实的数据
        with open('%s/%s' % (self.client_dir, file_name), 'wb') as f:
            recv_size = 0
            while recv_size < total_size:
                line = self.socket.recv(1024)
                f.write(line)
                recv_size += len(line)
                print('总大小%s,已下载%s' % (total_size, recv_size))

    def show(self, cmds):
        header = self.socket.recv(4)
        header_size = struct.unpack('i', header)[0]
        # 第二步：收报头数据
        header_bytes = self.socket.recv(header_size)

        # 第三步：取报头信息
        header_json = header_bytes.decode('utf-8')
        header_dic = json.loads(header_json)
        total_size = header_dic['total_size']

        # 第四步：接收真实的数据
        recv_size = 0
        recv_data = b''
        while recv_size < total_size:
            res = self.socket.recv(1024)
            recv_data += res
            recv_size += len(res)
        print(recv_data.decode('gbk'))  # linux用utf-8解码，windows用gbk解码

    def cd(self, cmds):
        print(cmds[1])
        if cmds[1] == '..' and self.user_dir != self.user_name:
            new_dir = self.user_dir.split('\\')
            new_dir.pop()
            self.user_dir = '\\'.join(new_dir)
        elif cmds[1] and cmds[1] != '..':
            self.user_dir = self.user_dir + '\\' + cmds[1]


# client = FTPClient(('127.0.0.1', 8090))
# client.run()
