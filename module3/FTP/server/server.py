#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket
import json
import struct
import subprocess
import os


class FTPServer:
    address_type = socket.AF_INET
    socket_type = socket.SOCK_STREAM
    allow_reuse_address = False
    max_packet_size = 8192
    coding = 'utf-8'
    request_queue_size = 5
    server_dir = 'share'

    def __init__(self, server_address, bind_active=True):
        self.server_address = server_address
        self.socket = socket.socket(self.address_type, self.socket_type)

        if bind_active:
            try:
                self.server_bind()
                self.server_active()
            except:
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
                    if cmds[0] == 'get':
                        get(self.conn, cmds)
                    elif cmds[0] == 'put':
                        put(self.conn, cmds)

                except ConnectionResetError:  # windows系统用try处理客户端断开报错退出
                    break
            self.conn.close()
        self.server_close()

