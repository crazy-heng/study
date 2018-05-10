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
    client_dir = os.path.join(BASE_DIR, 'download')

    def __init__(self, server_address, user_name, user_info, connect=True):
        self.server_address = server_address
        self.user_name = user_name
        self.user_info = user_info
        self.socket = socket.socket(self.address_type, self.socket_type)
        self.user_dir = user_name
        self.user_quota = 0
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
            self.socket.send(('%s /s' % self.user_name).encode('utf-8'))  # windows系统取配额
            self.user_quota = self.get_quota(cmds)
            self.socket.send(('%s %s' % (self.user_dir, cmds)).encode('utf-8'))
            cmd = cmds.split()
            if cmd[0] == 'get':
                self.get(cmd)
            elif cmd[0] == 'put':
                self.put(cmd)
            elif cmd[0] == 'dir':
                print(self.show(cmd))
            elif cmd[0] == 'cd':
                self.cd(cmd)
            else:
                print('请输入正确指令(get\put\dir\cd)')

            print('当前所在服务器目录%s' % self.user_dir)
        # self.client_close()

    def put(self, cmds):
        cmd = cmds[0]
        filename = cmds[1]
        filesize = 0
        file_dir = os.path.join(self.client_dir, filename)
        md5 = None
        if not os.path.isfile(file_dir):
            print('file:%s is not exists' % file_dir)
            filename = None
        else:
            filesize = os.path.getsize(file_dir)
            with open(file_dir, 'rb') as f:
                md5 = tools.md5(f.read())
        # 判断上传文件是否超过剩余配额
        if filesize > self.user_info[self.user_name][1] - int(self.user_quota):
            print('无法上传%s！当前剩余配额%s！' % (filesize, self.user_info[self.user_name][1] - int(self.user_quota)))
            filename = None

        head_dic = {'cmd': cmd, 'md5': md5, 'file_name': filename, 'file_size': filesize}
        # # print(head_dic)
        # head_json = json.dumps(head_dic)
        # head_json_bytes = bytes(head_json, encoding=self.coding)
        #
        # head_struct = struct.pack('i', len(head_json_bytes))
        # self.socket.send(head_struct)
        # self.socket.send(head_json_bytes)
        self.send(head_dic)
        send_size = 0
        if filename:
            with open(file_dir, 'rb') as f:
                for line in f:
                    self.socket.send(line)
                    send_size += len(line)
                    print('已传送%s!' % send_size)
                else:
                    print('upload successful')

    def get(self, cmds):
        header_dic = self.receive()
        total_size = header_dic['file_size']
        file_name = header_dic['file_name']
        md5_server = header_dic['md5']
        if file_name:
            # 第四步：接收真实的数据
            with open('%s/%s' % (self.client_dir, file_name), 'wb') as f:
                recv_size = 0
                while recv_size < total_size:
                    line = self.socket.recv(1024)
                    f.write(line)
                    recv_size += len(line)
                    print('总大小%s,已下载%s' % (total_size, recv_size))
            with open('%s/%s' % (self.client_dir, file_name), 'rb') as f:
                md5_local = tools.md5(f.read())
            if md5_local == md5_server:
                print('下载文件%s验证成功，下载完成！' % file_name)
            else:
                print('下载文件%s与服务器不一致，建议重新下载！' % file_name)
        else:
            print('%s无此文件！' % cmds[1])

    def show(self, cmds):
        header_dic = self.receive()
        total_size = header_dic['total_size']
        # 接收真实的数据
        recv_size = 0
        recv_data = b''
        while recv_size < total_size:
            res = self.socket.recv(1024)
            recv_data += res
            recv_size += len(res)
        return recv_data.decode('gbk')  # linux用utf-8解码，windows用gbk解码

    def cd(self, cmds):
        if cmds[1] == '..' and self.user_dir != self.user_name:
            new_dir = self.user_dir.split('\\')
            new_dir.pop()
            self.user_dir = '\\'.join(new_dir)
        elif cmds[1] and cmds[1] != '..':
            self.user_dir = self.user_dir + '\\' + cmds[1]

    def get_quota(self, cmds):  # 获取用户目录的使用量
        with open('temp', 'w', encoding='utf-8') as f:
            f.write(self.show(cmds))
        with open('temp', 'r', encoding='utf-8') as f:
            lines = len(f.readlines())
        with open('temp', 'r', encoding='utf-8') as f:
            i = 0
            for line in f.readlines():
                i += 1
                if i == lines - 3:
                    return line.strip().split(' ')[-2]

    def receive(self):
        header = self.socket.recv(4)
        header_size = struct.unpack('i', header)[0]
        # 第二步：收报头数据
        header_bytes = self.socket.recv(header_size)
        # 第三步：取报头信息
        header_json = header_bytes.decode('utf-8')
        header_dic = json.loads(header_json)
        return header_dic

    def send(self, head_dic):
        head_json = json.dumps(head_dic)
        head_json_bytes = bytes(head_json, encoding=self.coding)
        head_struct = struct.pack('i', len(head_json_bytes))
        self.socket.send(head_struct)
        self.socket.send(head_json_bytes)