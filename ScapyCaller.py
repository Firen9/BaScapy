from scapy.all import *
import MyGui
from Tkinter import *

def createPacket(werte):
    if not werte[0]:
        print("Geben Sie bitte eine IP ein")
    else:
        packet = IP(dst=werte[0]) / TCP()
        ip = True
    if not werte[1]:
        print("Gib Port ein")
    else:
        packet.dport = int(werte[1])
        port = True
    if werte[2]:
        packet.sport = int(werte[2])
    if werte[3]:
        packet.ack = int(werte[3])
    if werte[4]:
        packet.dataofs = int(werte[4])
    if werte[5]:
        packet.reserved = int(werte[5])
    if werte[6]:
        packet.flags = int(werte[6])
    if werte[7]:
        packet.urgptr = int(werte[7])
    if werte[8]:
        packet.options = werte[8]
    if ip and port:
        antwort=sr1(packet)

        answerWindow(antwort)
    else:
        print("IP oder Port eingeben")

def answerWindow(antwortPacket):
    answer = MyGui.Toplevel()
    msg = Message(answer, text=antwortPacket)

    msg.pack()


def test():
    hallo = "test"
    print(hallo)

def darstellung(self):
        """prints a summary of each packet with the packet's number
prn:     function to apply to each packet instead of lambda x:x.summary()
lfilter: truth function to apply to each packet to decide whether it will be displayed"""
        prn = None
        lfilter = None
        for i in range(len(self.res)):
            if lfilter is not None:
                if not lfilter(self.res[i]):
                    continue
            print conf.color_theme.id(i,fmt="%04i")
            if prn is None:
                print self._elt2sum(self.res[i])
            else:
                print prn(self.res[i])