import socket

def netcat(hostname, port, content):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((hostname, port))
    while 1:
        data = s.recv(1024)
        if data == "":
            break
        a = repr(data.decode("utf-8")).replace("'", '').split('\\n')
        for clam in a:
                if clam != '':
                        if clam not in clam_list:
                                print(clam)
                                s.send(b'clamclam\n')
                                print('SENDING')
    s.shutdown(socket.SHUT_WR)
    print("Connection closed.")
    s.close()

clam_list = ['clam{clam_clam_clam_clam_clam}', 'malc{malc_malc_malc_malc_malc}']
netcat('misc.2020.chall.actf.co', 20204, '')
