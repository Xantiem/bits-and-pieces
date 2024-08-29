import network
import time

class Net:
    def __init__(self):
        self.retry = 5
        self.net = ''
        self.ssid = ''
        self.phrase = ''

    def activate(self):
        self.net = network.WLAN(network.STA_IF)
        self.net.active(True)

        return self.net
    
    def attempt_connect(self):
        if self.phrase == '':
            self.net.connect(self.ssid)
        else:
            self.net.connect(self.ssid, self.phrase)
        return self.net.isconnected()
    
    def connect(self, ssid, phrase):
        self.ssid = ssid
        self.phrase = phrase


        Net.activate()
        time.sleep(4)
        if 


    
def connect(ssid, phrase):
    pass