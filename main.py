import socket
from _thread import *

##################Backend###################
#Utils
def fileget(name):
    pass
def filenamesget(name):
    pass
#Low level networking
def look_for_friends():
    while True:
        for i in friends.difference(ac):
            server.connect(i)
def connection_man():
    ac=friends
    start_new_thread(look_for_friends)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((IP_address, 69))
    server.listen(100)
    while True:
        conn, addr = server.accept()
        ac.update(conn)
        
def send(who,what):
    who.send(repr(what))
def send_req(who,wath):
    online=send(who,what)
    if online:
        while responsebuffer[who]==b'':
            time.sleep(0.01)
        r=responsebuffer[who]
        responsebuffer[who]=b''
        return r
def get_req(u):
    if u.isinstance(dict):
        globals()[u[0]](u[1])
    else:
        responsebuffer=u
#High level networking
def get_after(forwho,time):
    u=set()
    for i in filenamesget():
        if time<int(i[:i.find('.')]):
            break
        u.update(fileget(i))
    send(forwho,i)

def get_net(iter):
    if iter!=0:
        f=set()
        for i in friends:
            f.update(send_req(i,['get_net',(iter-1)]))
        send(forwho,f)
    else:
        send(forwho,friends)

def get_new_friends():
    f=set()
    for i in friends:
        f.update(send_req(i,['get_net',4]))
    return f.difference(friends)
    
