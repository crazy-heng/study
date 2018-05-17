#!/usr/bin/env python
# -*- coding: utf-8 -*-
from socket import *
import time

server = socket(AF_INET, SOCK_DGRAM)
server.bind(('127.0.0.1', 8095))

while True:
    data, client_addr = server.recvfrom(1024)
    print(data, client_addr)
    server_time = str(time.time())

    server.sendto(server_time.encode('utf-8'), client_addr)
