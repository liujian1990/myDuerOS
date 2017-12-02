import httplib
import time
#control light
conn =httplib.HTTPConnection("192.168.1.13",80)
def on():
    conn.request("GET", url="/on")
    print conn.getresponse().read()

def off():
    conn.request("GET", url="/off")
    print conn.getresponse().read()

#on()
#time.sleep(25)
#off()