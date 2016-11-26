from scapy.all import *
import MyGui
from Tkinter import *
import sys
from StringIO import StringIO
from scapy.layers import inet


def createPaket(values, fuzzing):
    if not values[0]:
        print("Geben Sie bitte eine IP ein")
    else:
        paket = IP(dst=values[0]) / TCP()
        ip = True
    if not values[1]:
        print("Gib Port ein")
    else:
        paket.dport = int(values[1])
        port = True
    if values[2]:
        paket.sport = int(values[2])
    if values[3]:
        paket.ack = int(values[3])
    if values[4]:
        paket.dataofs = int(values[4])
    if values[5]:
        paket.reserved = int(values[5])
    if values[6]:
        paket.flags = int(values[6])
    if values[7]:
        paket.window = int(values[6])
    if values[8]:
        paket.urgptr = int(values[7])
    if values[9]:
        paket.options = values[8]
    if ip and port:
        if not fuzzing:
            sendtest = catchingAnswer(paket)
            answer = sr1(paket)
            answertest = catchingAnswer(answer)
            # An Fenster senden
            MyGui.answerWindow(sendtest, answertest)
        else:
            sfuzzPakets = []
            afuzzPakets = []
            i = 0
            while i < int(values[10]):
                fuzzing = fuzz(paket)
                sFuzz = catchingAnswer(fuzzing)
                sfuzzPakets.append(sFuzz)
                #send(fuzzing)
                answerFuzz = sr1(fuzzing, inter=0.1, retry=0, timeout=0.1)
                #answerFuzz=1
                if answerFuzz is None:
                    afuzzPakets.append("Keine Antwort")
                else:
                #if isinstance(answerFuzz,basestring):
                    aFuzz = catchingAnswer(answerFuzz)
                    afuzzPakets.append(aFuzz)
                #else:
                   # afuzzPakets.append("Keine Antwort")
                i += 1
            MyGui.fuzzingWindow(sfuzzPakets, afuzzPakets)

    else:
        print("IP oder Port eingeben")


def catchingAnswer(paket):
    capture = StringIO()
    save_stdout = sys.stdout
    sys.stdout = capture
    paket.show()
    sys.stdout = save_stdout
    return capture.getvalue()
