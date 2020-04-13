import socket
import itertools

init_list = []
count = 1
for i in range(0, 20):
    if count > 0:
        init_list.append(1)
        count = count - 1
    else:
        init_list.append(0)

#ss = list(itertools.permutations(init_list))
for item in itertools.permutations(init_list):
    print(item)

def netcat(hostname, port, content):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((hostname, port))

    print(s.recv(1024).decode('utf-8'))
    s.send(str.encode('2\n'))

    while 1:
        data = s.recv(1024).decode('utf-8')
        print(data)
        if data == "":
            return
        if '?' in data:
            s.send(str.encode('no\n'))
        else:
            break

    s.shutdown(socket.SHUT_WR)
    print("Connection closed.")
    s.close()

netcat('challenges.tamuctf.com', 7393, '')
