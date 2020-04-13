import socket
import math

##def max_prime_factor(n):
##    '''find the largest prime factor of integer n'''
##
##    largest_factor = 1
##    i = 2
##
##    # i is a possible *smallest* factor of the (remaining) number n.
##    # If i * i > n then n is either 1 or a prime number.
##    while i * i <= n:
##        if n % i == 0:
##            largest_factor = i
##            # Divide by the highest possible power of the found factor:
##            while n % i == 0:
##                n //= i
##        i = 3 if i == 2 else i + 2
##
##    if n > 1:
##        # n is a prime number and therefore the largest prime factor of the 
##        # original number.
##        largest_factor = n
##
##    return largest_factor

def max_prime_factor(n):
    p = 10000000
    while 1:
        if (n / p).is_integer():
            return p
        else:
            p = p - 1
        
def netcat(hostname, port, content):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((hostname, port))

    print(s.recv(1024).decode('utf-8'))

    s.send(str.encode('\n'))
    
##    while 1:
    data = s.recv(1024)
    print(data.decode('utf-8'))
    if data == "":
        return
    a = data.decode('utf-8')
    p = max_prime_factor(int(a))
    print(str(int(p)) + ' ' + str(int(int(a) / int(p))))
    s.send(str.encode(str(int(p)) + ' ' + str(int(int(a) / int(p))) + '\n'))
    print(s.recv(1024).decode('utf-8'))
    print(s.recv(1024).decode('utf-8')) 
        
    s.shutdown(socket.SHUT_WR)
    print("Connection closed.")
    s.close()

netcat('challenges.tamuctf.com', 8573, '')
