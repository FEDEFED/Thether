import socket
from _thread import *


#############> Backend <#############
my_address=
terminate_char=
friends=

#Utils
def fileget(name):
    pass

def filenamesget(name):
    pass

#Low level networking
def look_for_friends():
    while True:
        for i in friends.difference(ac): #&
            server.connect(i)

def connection_man():
    ac=set()
    requestbuffer={}
    responsebuffer={}
    start_new_thread(look_for_friends)
    start_new_thread(get_reqs)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((my_address, 69))
    server.listen(100)
    while True:
        conn, addr = server.accept()
        if conn:
            ac.update(conn)
            responsebuffer.update({conn:b''})
            requestbuffer.update({conn:b''})

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

def get_reqs():
    while True:
        for i in ac:
            mess = i.recv(2048)
            requestbuffer[who]+=mess
            if terminate_char in requestbuffer:
                if u.isinstance(dict):
                    globals()[u[0]](u[1])
                else:
                    responsebuffer[who]=u
                requestbuffer=b''

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

def get_new_friends():
    f=set()
    for i in friends:
        f.update(send_req(i,['get_net',4]))
    return f.difference(friends)

#############> Frontend <#############
from kivy.lang import Builder
from kivymd.app import MDApp

KV='''
MDScreen:
    MDBottomNavigation:
        #panel_color: "#eeeaea"
        selected_color_background: "orange"
        text_color_active: "lightgrey"
        MDBottomNavigationItem:
            name: 'chats'
            text: 'chat'
            icon: 'chat'

            MDLabel:
                text: 'Y net'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'net'
            text: 'the net'
            icon: 'spider-web'

            MDLabel:
                text: 'Thethers'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'explore'
            text: 'xplore'
            icon: 'map-search'

            MDLabel:
                text: 'Y net'
                halign: 'center'
'''

class Test(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)


Test().run()
