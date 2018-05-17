#!/usr/bin/env python
# -*- coding: utf-8 -*-
from socket import *
import time

client = socket(AF_INET, SOCK_DGRAM)

while True:
    msg = input('-->>').strip()
    client.sendto(msg.encode('utf-8'), ('127.0.0.1', 8095))

    data, server_addr = client.recvfrom(1024)
    print(data, server_addr)
    print('server_time:%s' % data.decode('utf-8'))
    print(time.ctime(float(data.decode('utf-8'))))
client.close()
