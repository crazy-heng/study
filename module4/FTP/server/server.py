#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket
import json
import struct
import os
import hashlib
from concurrent.futures import ThreadPoolExecutor
from threading import Thread
import queue

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class FTPServer:
    address_type = socket.AF_INET
    socket_type = socket.SOCK_STREAM
    allow_reuse_address = False
    max_packet_size = 8192
    coding = 'utf-8'
    request_queue_size = 5
    server_dir = os.path.join(BASE_DIR, 'share')
    max_thread = 2  # 最大并发数
    run_thread = 0  # 运行进程数
    max_conn = 50   # 最大队列长度

    def __init__(self, server_address, bind_active=True):
        self.server_address = server_address
        self.socket = socket.socket(self.address_type, self.socket_type)
        self.q = queue.Queue(self.max_conn)
        # self.pool = ThreadPoolExecutor(self.thread)

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
            conn, client_address = self.get_request()
            print('from client', client_address)
            # self.pool.submit(self.communicate, conn)
            if self.run_thread >= self.max_thread:  # 判断是否达到最大并发，达到则排队，没达到创建进程
                self.q.put(conn)
                self.tell_client(conn)
            else:
                self.make_thread(conn)

    def tell_client(self, conn):  # 告知等待的客户端当前排队数
        try:
            msg = 'wait,%d' % len(self.q.queue)
            conn.send(msg.encode('utf-8'))
        except ConnectionResetError:
            return

    def make_thread(self, conn):  # 创建进程并发处理
        try:
            conn.send('success'.encode('utf-8'))
            t = Thread(target=self.communicate, args=(conn,))
            t.start()
            self.run_thread += 1
        except ConnectionResetError:
            return False

    def communicate(self, conn):
        while True:
            try:
                # 1 接收命令
                head_dic = self.receive(conn)
                if not head_dic:
                    break
                print('客户端数据', head_dic)
                cmd = head_dic['cmd']
                if hasattr(self, cmd):
                    func = getattr(self, cmd)
                    func(conn, head_dic)
            except ConnectionResetError:  # 当有用户退出后，排队队列里排队链接登录，并通知其它等待用户
                while self.make_thread(self.q.get()) is False:
                    pass
                else:
                    for i in self.q.queue:
                        self.tell_client(i)
                    self.run_thread -= 1
                break
        conn.close()

    def put(self, conn, cmd):
        user_dir = cmd['user_dir']
        file_name = cmd['file_name']
        file_dir = os.path.join(self.server_dir, user_dir, file_name)
        print(file_dir)
        # 判断下载文件是否存在
        if not os.path.isfile(file_dir):
            print('服务器上无此文件%s' % file_name)
            file_name = None
            file_size = 0
            md5 = 0
        else:
            file_size = os.path.getsize(file_dir)
            md5 = self.md5(file_dir)
        # 第一步 制作报头,struct模块用i格式固定长度是4
        header_dic = {'file_name': file_name, 'md5': md5, 'file_size': file_size}
        self.send(conn, header_dic)
        head_dic = self.receive(conn)
        file_size = head_dic['file_size']
        if head_dic['file_flag'] == 0 and file_name:
            with open(file_dir, 'rb') as f:
                f.seek(file_size)
                for line in f:
                    conn.send(line)

    def get(self, conn, cmd):
        user_dir = cmd['user_dir']
        # header_dic = self.receive(conn)
        total_size = cmd['file_size']
        file_name = cmd['file_name']
        md5_upload = cmd['md5']
        # 接收真实的数据
        file_dir = os.path.join(self.server_dir, user_dir, file_name)
        file_flag = 0
        if os.path.exists(file_dir):  # 判断服务器上是否已有文件
            file_size = os.path.getsize(file_dir)
            if file_size == total_size and self.md5(file_dir) == md5_upload:  # 判断是否需要续传
                file_flag = 1
        else:
            file_size = 0
        header_dic = {'file_size': file_size, 'file_flag': file_flag}
        self.send(conn, header_dic)
        if file_flag == 1:  # 已有相同文件不再接收
            return
        with open(file_dir, 'ab') as f:
            recv_size = file_size
            while recv_size < total_size:
                line = conn.recv(1024)
                f.write(line)
                recv_size += len(line)
                print('总大小%s,已下载%s' % (total_size, recv_size))
        md5_local = self.md5(file_dir)
        if md5_local == md5_upload:
            print('上传传文件%s验证md5[%s]成功，上传完成！' % (file_name, md5_local))
        else:
            print('上传文件%s与服务器不一致，建议重新上传！' % file_name)

    def dir(self, conn, cmd):
        path = os.path.join(self.server_dir, cmd['user_dir'])
        if os.path.exists(path):
            dirs = '\n'.join(os.listdir(path))
            header_dic = {'total_size': len(dirs)}
            self.send(conn, header_dic)
            for file in dirs:
                conn.send(file.encode(self.coding))
        else:
            header_dic = {'total_size': 0}
            self.send(conn, header_dic)

    def md5(self, file):
        with open(file, 'rb') as f:
            m = hashlib.md5()
            m.update(f.read())
            return m.hexdigest()

    def receive(self, conn):  # 接收报头并返回数据
        header = conn.recv(4)
        if not header:
            return None
        header_size = struct.unpack('i', header)[0]
        header_bytes = conn.recv(header_size)
        header_json = header_bytes.decode(self.coding)
        header_dic = json.loads(header_json)
        return header_dic

    def send(self, conn, header_dic):  # 发送报头
        header_json = json.dumps(header_dic)
        header_bytes = header_json.encode(self.coding)
        header = struct.pack('i', len(header_bytes))
        conn.send(header)
        conn.send(header_bytes)

    def quota(self, conn, header_dic):
        user_name = header_dic['user_name']
        user_dir = os.path.join(self.server_dir, user_name)
        size = 0
        for root, dirs, files in os.walk(user_dir):
            size += sum([os.path.getsize(os.path.join(root, name)) for name in files])
        header_dic = {'quota': size}
        self.send(conn, header_dic)
