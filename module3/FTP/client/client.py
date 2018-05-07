#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import struct
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class FTPClient:
    address_type = socket.AF_INET
    socket_type = socket.SOCK_STREAM
    allow_reuse_address = False
    max_packet_size = 8192
    coding = 'utf-8'
    request_queue_size = 5
    client_dir = BASE_DIR + '/download'

    def __init__(self, server_address, connect=True):
        self.server_address = server_address
        self.socket = socket.socket(self.address_type, self.socket_type)
        if connect:
            try:
                self.client_connect()
            except:
                self.client_close()
                raise

    def client_connect(self):
        self.socket.connect(self.server_address)

    def client_close(self):
        self.socket.close()

    def run(self):
        while True:
            # 1 发命令
            cmd = input('-->').strip()
            if not cmd:
                continue
            self.socket.send(cmd.encode('utf-8'))
            cmds = cmd.split()
            if cmds[0] == 'get':
                self.get(cmds)
            elif cmds[0] == 'put':
                self.put(cmds)

        self.client_close()

    def put(self, cmds):
        cmd = cmds[0]
        filename = cmds[1]
        if not os.path.isfile('%s/%s' % (self.client_dir, filename)):
            print('file:%s/%s is not exists' % (self.client_dir, filename))
            return
        else:
            filesize = os.path.getsize('%s/%s' % (self.client_dir, filename))

        head_dic = {'cmd': cmd, 'file_name': filename, 'file_size': filesize}
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


client = FTPClient(('127.0.0.1', 8080))
client.run()
