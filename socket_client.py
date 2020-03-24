#!/usr/bin/python
# *-* coding: utf-8*-*

from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 8000))
s.listen(1)
print 'connect waiting.....'
conn, addr = s.accept()
print 'connected by', addr

while 1:
    data = conn.recv(1024)
    if not data:
        break
    print 'recive_data:', data
    conn.send(data)

conn.close()
s.close()

