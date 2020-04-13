# -*- coding: utf-8 -*-
"""
Created for Spring 2020 CTF
Cryptography 1 
40 Points
Welcome to the one time pad oracle! 
Our oracle's function is enc := key ^ msg | dec := key ^ ct
The oracle is found at umbccd.io:13371, and your methods are:
    flg - returns the encrypted flag
    enc - returns the encryption of the message after the : in "enc:..."
    dec - returns the decryption of the ciphertext after the : in "dec:..."
    
@author: pleoxconfusa
"""

import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('crypto.ctf.umbccd.io', 13371)
sock.connect(server_address)

#available methods: flg, enc, dec.


msg = 'flg'.encode()
sock.sendall(msg)
flg = sock.recv(1024)
print(flg) #not decoded, because now the oracle sends encrypted bytes.

# b'r\xb2\xe1\xac\x15\xfeP\xae\x7f\x18\xe4\\\xe6\x17\x9e1\x9a\x1c7j\x0fB2\xc3\x0b\xd5r\xbf\xa6\xef\xed\xc4\x1a\xcf`N\xd6k\x12\xb4\xb1K'
# Encrypted flag ^

msg = 'enc:LET ME IN!!!'.encode()
sock.sendall(msg)
enc = sock.recv(1024) 
print(enc)

# LET ME IN!!! ^ KEY = b'z\x96\xc2\xeb\x1b\xef6\x9cay\xa1\x19\x8fy\xf9n\xd7,EYP\x0e\x03\x888\x8a!\xff\xc2\x8b\x84\xaa}\x90 #\xbf\x193\x83\x826'
# ... ^ KEY = LET ME IN!!!

msg = b'dec:' + enc
sock.sendall(msg)
dec = sock.recv(1024)
print(dec) #sanity check

def byte_xor(ba1, ba2):
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])

key = byte_xor(enc, dec)
print(byte_xor(key, flg))
    
sock.close()
