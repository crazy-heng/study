#!/usr/bin/env python
# -*- coding: utf-8 -*-
from socket import *

server = socket(AF_INET, SOCK_DGRAM)
server.bind(('127.0.0.1', 8095))

while True:
    data, client_addr = server.recvfrom(1024)
    print(data, client_addr)

    server.sendto(data.upper(), client_addr)
