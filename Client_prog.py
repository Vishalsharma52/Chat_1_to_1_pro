#!/usr/bin/env python
# coding: utf-8

# In[40]:


import socket
from threading import Thread


# In[42]:


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ip = input("entre the ip address : - ")
port = int(input("entre the port : - "))

s.connect((ip,port))


# In[43]:


def send():
    while True:
        msg = input("Entre your msg:-")
        s.send(msg.encode())


# In[44]:


def recv():
    while True:
        x = s.recv(1024)
        print(x.decode())
        


# In[45]:


x1 = Thread(target = send)


# In[46]:


x2 = Thread(target = recv)


# In[48]:


x1.start()
x2.start()


# In[ ]:




