# -*- coding: utf-8 -*-

import socket
import struct
import time
import random
import json
#竟然是http协议
url="http://192.168.1.7:6095/general?action=getVolum"
host='192.168.1.7'
port=9093
### app名称 appname
bzhan="com.bilibili.tv"
tv="com.dianshijia.newlive"
###
final={"vercode":1,"clientId":1008156}
first_cmd=[
0x55, 0x20, 0x0a, 0x00, 0x00, 0x00, 0x00, 0x10,
0x00, 0x00, 0x01, 0x0f, 0x27, 0x10, 0x04, 0x02,
0x00, 0x00, 0x00, 0xe3, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x20]

data0 = struct.pack("%dB" % (len(first_cmd)), *first_cmd)

def getapp(appname):
    timeup=str(int(round(time.time() * 1000)))+str(random.random())

    seltv= {
        "request":"true",
        "requestId":timeup,
        "action":0,
        "control":{
            "type":0,
            "method":{
                "methodCallID":0,
                "methodName":"openApp",
                "methodCall":{
                "args":[appname,""],
                "useDataChannelReturn":"true"
                }
            }
        }
    }

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.connect((host, port))
    except socket.error as msg:
        s.close()
        print port, ":", msg

    databody=json.dumps(seltv)+json.dumps(final)
    data=data0+databody.replace(' ','')

    s.sendall(data)
    print s.recv(1024)
    s.close()

