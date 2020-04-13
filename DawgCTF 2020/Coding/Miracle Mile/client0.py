# -*- coding: utf-8 -*-
"""
Created for Spring 2020 CTF
Cryptography 0
10 Points
Welcome to my sanity check.  You'll find this to be fairly easy.  
The oracle is found at umbccd.io:13370, and your methods are:
    flg - returns the flag
    tst - returns the message after the : in "tst:..."
    
@author: pleoxconfusa
"""

import socket
import math

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('ctf.umbccd.io', 5300)
sock.connect(server_address)

#sock.sendall(msg.encode())
data = sock.recv(1024)

while 1:
    data = sock.recv(1024)
    print(data.decode())

    no = data.decode().split('I ran ')[1].split(' ')[0]
    time = data.decode().split(' in ')[1].split(' ')[0]

    print(no)
    print(time)

    curr_sec = time.split(':')[2]
    curr_min = time.split(':')[1]
    curr_hour = time.split(':')[0]

    new_min = int(curr_min) + int(curr_hour) * 60
    new_sec = int(curr_sec) + int(new_min) * 60
    new_sec_div = new_sec / int(no)

    print(new_sec_div)
    print(math.floor(new_sec_div))
    sec = math.floor(new_sec_div) % 60
    print(sec)
    minute = (math.floor(new_sec_div) - sec) / 60
    print(str(int(minute)) + ':' + str(sec) + ' minutes/mile')
    sock.sendall(str.encode(str(int(minute)) + ':' + str(sec) + ' minutes/mile'))

#sock.sendall()
sock.close()
