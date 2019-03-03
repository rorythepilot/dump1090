#!/usr/bin/python
import sys #for args
import subprocess
from datetime import datetime
from datetime import timedelta
import socket
import json
import time
#for wunderground weather station
import urllib2
import urllib
from threading import Timer

#https://stackoverflow.com/questions/3393612/run-certain-code-every-n-seconds
class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False
        
def checkNetwork():
    #is seanav ready and listening 
    server_address = ('54.225.196.162', 5114)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connected=False
    try: #dont exit if the receiving server is not running yet
        s.connect(server_address)
        connected=True
    except socket.error as msg:
        print "Socket Error connecting: %s" % msg
        connected=False
        pass
    if(connected) :
            s.close()
    return connected

def getAircraft():
    link = "http://localhost:8080/data/aircraft.json"
    f = urllib.urlopen(link)
    jsonmsg= f.read() 
    f.close
    #print jsonmsg
    return jsonmsg


def sendAircraft():
    
    jsonmsg= getAircraft()
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

    #strip the trailing carriage return \n
    #print jsonmsg 
    timestamp = datetime.now().strftime("%s")
    #server_address = ('54.225.196.162', 5114)
    server_address = ('127.0.0.1', 5114)
    try: #dont exit if the receiving server is not running yet
        message='{"adsb":{"id":'+str(portnumber)+',"data":'+jsonmsg.rstrip()+"}}\r\n"
        s.sendto(message, server_address) 
        #print "Socket sent: %s" % message
         
    except socket.error as msg:
        print "Socket Error connecting: %s" % msg
        pass  
      
localOnly=False;
portnumber = sys.argv[1]
if (len(sys.argv) >2 and len(sys.argv[2]) > 1):
    localOnly=sys.argv[2];



#write latest measurements to local file
if localOnly: 
    #print "Going loco\r\n"    
    rt = RepeatedTimer(5, getAircraft) # it auto-starts, no need of rt.start()
    quit()
    
#send out  messages with readings
connected=False
#server_address = ('127.0.0.1', 5114)

startupMessageSent=False
  
print "Looping starting"
rt = RepeatedTimer(5, sendAircraft) # it auto-starts, no need of rt.start()
print "Looping ending"



    
      

