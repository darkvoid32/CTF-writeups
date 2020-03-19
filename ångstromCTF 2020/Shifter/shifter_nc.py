import socket
  
def fib_to(n):
    fibs = [0, 1]
    for i in range(2, n+1):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs

def encrypt(text,s): 
    result = "" 
  
    # traverse text 
    for i in range(len(text)): 
        char = text[i] 
  
        # Encrypt uppercase characters 
        if (char.isupper()): 
            result += chr((ord(char) + s-65) % 26 + 65) 
  
        # Encrypt lowercase characters 
        else: 
            result += chr((ord(char) + s - 97) % 26 + 97) 
  
    return result 
  
def netcat(hostname, port, content):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((hostname, port))
    while 1:
        data = s.recv(1024)
        if data == "":
            break
        print(repr(data.decode("utf-8")))
        shift = (repr(data.decode("utf-8"))).split('Shift ')[1].split(' ')[0]
        n = (repr(data.decode("utf-8"))).split('by n=')[1].split('\\n')[0]
        print('PT : ' + shift)
        print('No : ' + n)
        if n == 0:
            s.send(str.encode(shift + '\n'))
        else:
            fib = a[int(n)]
            print('Fi : ' + str(fib))
            cipher = encrypt(shift, fib)
            print('Ci : ' + cipher)
            s.send(str.encode(cipher + '\n'))
        
    s.shutdown(socket.SHUT_WR)
    print("Connection closed.")
    s.close()

a = fib_to(51)
netcat('misc.2020.chall.actf.co', 20300, '')
