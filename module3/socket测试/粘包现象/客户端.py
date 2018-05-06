#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 9000))

client.send('hello'.encode('utf-8'))
client.send('world'.encode('utf-8'))
