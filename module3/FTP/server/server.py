#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket
import json
import struct
import subprocess
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)


class FTPServer:
    address_type = socket.AF_INET
    socket_type = socket.SOCK_STREAM
    allow_reuse_address = False
    max_packet_size = 8192
    coding = 'utf-8'
    request_queue_size = 5
    server_dir = BASE_DIR + '/share'

    def __init__(self, server_address, bind_active=True):
        self.server_address = server_address
        self.socket = socket.socket(self.address_type, self.socket_type)

        if bind_active:
            try:
                self.server_bind()
                self.server_active()
            except Exception:
                self.server_close()
                raise

    def server_bind(self):
        if self.allow_reuse_address:
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(self.server_address)
        self.server_address = self.socket.getsockname()

    def server_active(self):
        self.socket.listen(self.request_queue_size)

    def server_close(self):
        self.socket.close()

    def get_request(self):
        return self.socket.accept()

    def close_request(self, request):
        request.close()

    def run(self):
        while True:
            self.conn, self.client_address = self.get_request()
            print('from client', self.client_address)
            while True:
                try:
                    # 1 接收命令
                    res = self.conn.recv(self.max_packet_size)
                    if not res:
                        break
                    print('客户端数据', res)

                    # 2 解析命令，提取相应命令参数
                    cmds = res.decode('utf-8').split()
                    if cmds[1] == 'get':
                        self.put(self.conn, cmds)
                    elif cmds[1] == 'put':
                        self.get(self.conn, cmds)
                    elif cmds[1] == 'dir':
                        self.show(self.conn, cmds)
                    elif cmds[1] == 'cd':
                        print('当前服务器目录%s' % cmds[0])
                except ConnectionResetError:  # windows系统用try处理客户端断开报错退出
                    break
            self.conn.close()
        # self.server_close()

    def put(self, conn, cmds):
        username = cmds[0]
        filename = cmds[2]
        # 第一步 制作报头,struct模块用i格式固定长度是4
        header_dic = {
            'file_name': filename,
            'md5': 'xxxeddexxx',
            'file_size': os.path.getsize('%s/%s' % (self.server_dir, filename))
        }
        print(header_dic)
        header_json = json.dumps(header_dic)
        header_bytes = header_json.encode('utf-8')
        # 第二步 发送报头长度
        header = struct.pack('i', len(header_bytes))
        conn.send(header)
        # 第三步：把报头数据发送给客户端
        conn.send(header_bytes)
        # 第四步：再发送真实数据
        with open('%s/%s/%s' % (self.server_dir, username, filename), 'rb') as f:
            for line in f:
                conn.send(line)

    def get(self, conn, cmds):
        username = cmds[0]
        print(username)
        header = conn.recv(4)
        header_size = struct.unpack('i', header)[0]
        # 第二步：收报头数据
        header_bytes = conn.recv(header_size)
        # 第三步：取报头信息
        header_json = header_bytes.decode('utf-8')
        header_dic = json.loads(header_json)
        total_size = header_dic['file_size']
        file_name = header_dic['file_name']
        # 第四步：接收真实的数据
        with open('%s/%s/%s' % (self.server_dir, username, file_name), 'wb') as f:
            recv_size = 0
            while recv_size < total_size:
                line = conn.recv(1024)  # 1024一个坑
                f.write(line)
                recv_size += len(line)
                print('总大小%s,已下载%s' % (total_size, recv_size))

    def show(self, conn, cmd):
        print('dir share\%s' % cmd[0])
        obj = subprocess.Popen('dir share\%s' % cmd[0], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout = obj.stdout.read()
        stderr = obj.stderr.read()
        # 第一步：制作报头,struct模块用i格式固定长度是4
        header_dic = {
            'filename': 'a.txt',
            'md5': 'xxxeddexxx',
            'total_size': len(stdout) + len(stderr)
        }
        header_json = json.dumps(header_dic)
        header_bytes = header_json.encode('utf-8')
        # 第二步 发送报头长度
        header = struct.pack('i', len(header_bytes))
        conn.send(header)
        # 第三步：把报头数据发送给客户端
        conn.send(header_bytes)
        # 第四步：再发送真实数据
        conn.send(stdout)
        conn.send(stderr)


server = FTPServer(('127.0.0.1', 8090))
server.run()
