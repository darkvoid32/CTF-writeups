import socket
import math

##def discreteLogarithm(a, b, m):  
##  
##    n = int(math.sqrt (m) + 1); 
##  
##    # Calculate a ^ n  
##    an = 1; 
##    for i in range(n): 
##        an = (an * a) % m; 
##  
##    value = [0] * m; 
##  
##    # Store all values of a^(n*i) of LHS 
##    cur = an; 
##    for i in range(1, n + 1): 
##        if (value[ cur ] == 0): 
##            value[ cur ] = i; 
##        cur = (cur * an) % m; 
##      
##    cur = b; 
##    for i in range(n + 1): 
##          
##        # Calculate (a ^ j) * b and check 
##        # for collision 
##        if (value[cur] > 0): 
##            ans = value[cur] * n - i; 
##            if (ans < m): 
##                return ans; 
##        cur = (cur * a) % m; 
##  
##    return -1;

def discreteLog2( prime, base, arg ):
    result = 0
    N = prime - 1
    n = 1 + int(N**1/2)
    firstList = {1:0}
    current = 1
    for i in range(1,n+1):
        current = current*base%prime
        if not current in firstList:
            firstList[current] = i
    if arg in firstList:
        return firstList[arg]
    else:
        multiplier = euclidean(pow(base,n,prime),prime)[1]%prime
        for i in range(1,n+1):
            arg = (arg*multiplier)%prime
            if arg in firstList:
                return(firstList[arg]+n*i)
    return(-1)

def netcat(hostname, port, content):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((hostname, port))
    while 1:
        data = s.recv(1024)
        if data == "":
            break
        # Print string & Get variables
        a = repr(data.decode("utf-8"))[1:-1].split('\\n')
        for string in a:
            print(string)
            if 'p =' in string:
                p = string[3:].strip()
            if 'a =' in string:
                a = string[3:].strip()
            if 'b =' in string:
                b = string[3:].strip()
        p = int(p)
        a = int(a)
        b = int(b)
##        # Solve
##        flag = False
##        for x in range(p):
##            if pow(a, x, p) == b:
##                print('x = ' + x)
##                s.send(str.encode(x + '\n'))
##                flag = True
##                break
##        if flag == False:
##            print('No x found :(')
        x = discreteLog2(a, b, p)
        s.send(str.encode(x + '\n'))
        s.send('='*30)
            
    s.shutdown(socket.SHUT_WR)
    print("Connection closed.")
    s.close()

netcat('crypto.2020.chall.actf.co', 20603, '')


##We define a^^b to be such that a^^0 = 1 and a^^b = a^(a^^(b-1)), where x^y represents x to the power of y.
##Given this, find a positive integer x such that a^^x = b mod p.

## I assume its (a ^^ x) % p = b 
## a^^b = a^(a^^(b-1)), where a ^^ 0 = 1 Recursive function for a ^ a ^ a....
