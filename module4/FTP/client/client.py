#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import struct
import json
import os
import tools
import setting
import time

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

    def run(self):  # 接收服务端信号，排队则继续等待
        recv = self.socket.recv(1024).decode('utf-8')
        while recv.split(',')[0] == 'wait':
            print('服务器连接数已满！当前等待人数%s' % recv.split(',')[1])
            time.sleep(5)
            recv = self.socket.recv(1024).decode('utf-8')
            if recv == 'success':
                print('登录服务器成功！')
                break
        else:
            print('登录服务器成功！')
        while True:
            # 1 发命令
            cmds = input('-->').strip()
            if not cmds:
                continue
            cmds = cmds.split()
            cmd = cmds[0]
            if cmd == 'dir' or len(cmds) >= 2:
                if hasattr(self, cmd):
                    func = getattr(self, cmd)
                    func(cmds)
            else:
                print('命令参数错误!')

            print('当前所在服务器目录%s' % self.user_dir)
        # self.client_close()

    def put(self, cmds):
        filename = cmds[1]
        file_dir = os.path.join(self.client_dir, filename)
        if not os.path.exists(file_dir):
            print('file:%s is not exists' % filename)
            return
        else:
            filesize = os.path.getsize(file_dir)
            md5 = tools.md5(file_dir)
        # 判断上传文件是否超过剩余配额
        self.get_quota()
        remain_quota = self.user_info[self.user_name][1] - int(self.user_quota)
        if filesize > remain_quota:
            print('无法上传%s！当前剩余配额%s！' % (filesize, remain_quota))
            return

        head_dic = {'cmd': 'get', 'md5': md5, 'file_name': filename, 'file_size': filesize, 'user_dir': self.user_dir}
        self.send(head_dic)
        header_dic = self.receive()
        send_size = header_dic['file_size']
        if header_dic['file_flag'] == 0:
            with open(file_dir, 'rb') as f:
                f.seek(send_size)
                for line in f:
                    self.socket.send(line)
                    send_size += len(line)
                    print('已传送%s!' % send_size)
                else:
                    print('upload successful')
        else:
            print('服务器上已有相同文件！')

    def get(self, cmds):
        filename = cmds[1]
        download_dir = os.path.join(self.client_dir, filename)
        head_dic = {'cmd': 'put', 'file_name': filename, 'user_dir': self.user_dir}
        self.send(head_dic)
        header_dic = self.receive()
        total_size = header_dic['file_size']
        file_name = header_dic['file_name']
        md5_server = header_dic['md5']
        file_size = 0
        file_flag = 0
        if os.path.exists(download_dir):  # 判断本地是否已有接收完成的文件
            file_size = os.path.getsize(download_dir)
            if file_size == total_size and tools.md5(download_dir) == md5_server:  # 判断是否是续传
                file_flag = 1
            else:
                file_flag = 0
        head_dic = {'file_size': file_size, 'file_flag': file_flag}
        self.send(head_dic)
        if file_flag == 0 and file_name:
            # 第四步：接收真实的数据
            with open(download_dir, 'ab') as f:
                recv_size = file_size
                while recv_size < total_size:
                    line = self.socket.recv(1024)
                    f.write(line)
                    recv_size += len(line)
                    print('总大小%s,已下载%s' % (total_size, recv_size))
            md5_local = tools.md5(download_dir)
            if md5_local == md5_server:
                print('下载文件%s验证成功，下载完成！' % file_name)
            else:
                print('下载文件%s与服务器不一致，建议重新下载！' % file_name)
        elif file_flag == 1:
            print('已下载过相同文件！')
        else:
            print('%s无此文件！' % filename)

    def dir(self, cmds):
        head_dic = {'cmd': 'dir', 'user_dir': self.user_dir}
        self.show(head_dic)

    def show(self, head_dic):
        self.send(head_dic)
        header_dic = self.receive()
        total_size = header_dic['total_size']
        # 接收真实的数据
        if total_size != 0:
            recv_size = 0
            recv_data = b''
            while recv_size < total_size:
                res = self.socket.recv(1024)
                recv_data += res
                recv_size += len(res)
            print(recv_data.decode(setting.coding))  # linux用utf-8解码，windows用gbk解码
        else:
            print('服务器上无%s目录' % self.user_dir)

    def cd(self, cmds):
        if cmds[1] == '..' and self.user_dir != self.user_name:
            self.user_dir = os.path.dirname(self.user_dir)
        elif cmds[1] and cmds[1] != '..':
            self.user_dir = self.user_dir + os.sep + cmds[1]

    def get_quota(self):  # 获取用户目录的使用量
        head_dic = {'cmd': 'quota', 'user_name': self.user_name}
        self.send(head_dic)
        header_dic = self.receive()
        self.user_quota = header_dic['quota']

    def receive(self):
        header = self.socket.recv(4)
        header_size = struct.unpack('i', header)[0]
        # 第二步：收报头数据
        header_bytes = self.socket.recv(header_size)
        # 第三步：取报头信息
        header_json = header_bytes.decode(self.coding)
        header_dic = json.loads(header_json)
        return header_dic

    def send(self, head_dic):
        head_json = json.dumps(head_dic)
        head_json_bytes = bytes(head_json, encoding=self.coding)
        head_struct = struct.pack('i', len(head_json_bytes))
        self.socket.send(head_struct)
        self.socket.send(head_json_bytes)