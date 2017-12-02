# -*- coding: utf-8 -*-

import socket
import struct
import binascii
import time
from micmd import *

cmd_counts=0x00
url="http://192.168.1.7:6095/general?action=getVolum"
host='192.168.1.7'
port=6091

shutupcmds=[shutdown, right_move,right_move,ok]

class mitv():
    def __init__(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((host, port))
        except socket.error as msg:
            s.close()
            exit(-1)
        print "Port",port,"Connected!"
        self.first()

    def first(self):
        data0 = struct.pack("%dB" % (len(first_cmd)), *first_cmd)
        self.s.sendall(data0)
        print "Recv system info:",self.s.recv(1024)

    def sendhandle(slef,cmds):
        global cmd_counts
        for cmd in cmds:    #cmd[0][8]
            cmd_counts=cmd_counts+1
            cmd[0][7]=cmd_counts
            data0 = struct.pack("%dB" % (len(cmd[0])), *cmd[0])
            cmd_counts=cmd_counts+1
            cmd[1][7]=cmd_counts
            data1 = struct.pack("%dB" % (len(cmd[1])), *cmd[1])

            slef.s.sendall(data0)
            print "recv:",str(binascii.b2a_hex(slef.s.recv(1024)))
            slef.s.sendall(data1)
            print "recv:",str(binascii.b2a_hex(slef.s.recv(1024)))
            time.sleep(1)
'''
first()

cmds=[
    esc,esc,
    voice_add,voice_add,
    voice_add, voice_add,
    voice_reduce,voice_reduce,
    voice_reduce, voice_reduce,
    menu, mainpage,
    shutdown, right_move,right_move,ok,shutdown
    ]
sendhandle(cmds)
s.close()
'''

