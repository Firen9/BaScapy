from scapy.all import *
import MyGui
from Tkinter import *
import sys
from StringIO import StringIO
from scapy.layers import inet

def createPacket(werte,fuzzing):
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
        packet.window = int(werte[6])
    if werte[8]:
        packet.urgptr = int(werte[7])
    if werte[9]:
        packet.options = werte[8]
    if ip and port:
        if not fuzzing:
            antwort=sr1(packet)
            test = ausgabeAbfangen(antwort)
            #An Fenster senden
            answerWindow(test)
        else:
            send(fuzz(packet),loop=1,count=int(werte[10]))

    else:
        print("IP oder Port eingeben")

def answerWindow(antwortPacket):
    answer = MyGui.Toplevel()
    msg = Message(answer, text=antwortPacket)

    msg.pack()


def ausgabeAbfangen(packet):
    capture = StringIO()
    save_stdout = sys.stdout
    sys.stdout = capture
    packet.show()
    sys.stdout = save_stdout
    return capture.getvalue()