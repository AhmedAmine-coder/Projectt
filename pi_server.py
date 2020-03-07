
from socket import *
from time import ctime
import struct
import numpy as np


ctrCmd = ['Up','Down']
HOST = ''
PORT = 50001
BUFSIZE = 1024
ADDR = (HOST,PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)


while True:
        print ('Waiting for connection')
        tcpCliSock,addr = tcpSerSock.accept()
        print ('...connected from :', addr)
        try:
                while True:
                        data = ''
                        data = tcpCliSock.recv(BUFSIZE)
                        ch=''
                        for word in range(len(data)) :
                                if data[word]>51:
                                        ch += chr(data[word])  
                        if not data:
                                break
                        if ch == "Up":
                                print ('Increase: ')
                        if ch == "testbarchamarrat":
                                print ('Decrease: ')
        except KeyboardInterrupt:
                tcpSerSock.close()
tcpSerSock.close()
