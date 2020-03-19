import socket
import base64
import random
import time
import string

# Same as OTP
def decode(a, b):
        r = ""
        for i, j in zip(a, b):
                r += chr(ord(i) ^ ord(j))
        return r

def netcat(hostname, port, content):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    random.seed(int(time.time()))
    p_init = ''.join([string.ascii_letters[random.randint(0, len(string.ascii_letters)-1)] for _ in range(random.randint(1, 30))])
    k_init = ''.join([string.ascii_letters[random.randint(0, len(string.ascii_letters)-1)] for _ in range(len(p_init))])
    print(p_init)
    print(k_init)
    
    s.connect((hostname, port))
    data = s.recv(1024)
    print(repr(data.decode("utf-8")))
    s.send(str.encode('2\n'))
    while 1:
        data = s.recv(1024)
        if data == "":
            break
        print(repr(data.decode("utf-8")))
##        x = repr(data.decode("utf-8")).replace("'", '').split('\\n')[0]
##        x_dec = base64.b64decode(x).decode('utf-8')
##        k = repr(data.decode("utf-8")).replace("'", '').split('key ')[1]
##        k_dec = base64.b64decode(k).decode('utf-8')
##        print('Given Key : ' + k_dec)

        s.send(str.encode(p_init+ '\n'))
        
    s.shutdown(socket.SHUT_WR)
    print("Connection closed.")
    s.close()

netcat('misc.2020.chall.actf.co', 20301, '')
