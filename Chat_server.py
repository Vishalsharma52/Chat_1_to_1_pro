import socket
import threading
import time

AF = socket.AF_INET
Myp = socket.SOCK_STREAM

s = socket.socket(AF,Myp)

ip = ""
port = 2222

s.bind((ip,port))

s.listen()
 
i , j = s.accept()

def rec(i,j):
    while True:
        x=i
        y=j
        msg = x.recv(1024)
        print(y , ":", msg.decode() )
def send(i):
    while True:
        x=i
        msg = input("Entre your msg :- ")
        x.send(msg.encode())


x1 = threading.Thread( target = rec, args= (i,j))
x2 = threading.Thread( target = send, args= (i,))

x2.start()
x1.start()




