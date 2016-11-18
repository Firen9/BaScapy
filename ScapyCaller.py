from scapy.all import *
import MyGui
from Tkinter import *
import sys
from StringIO import StringIO
from scapy.layers import inet


def createPaket(werte, fuzzing):
    if not werte[0]:
        print("Geben Sie bitte eine IP ein")
    else:
        paket = IP(dst=werte[0]) / TCP()
        ip = True
    if not werte[1]:
        print("Gib Port ein")
    else:
        paket.dport = int(werte[1])
        port = True
    if werte[2]:
        paket.sport = int(werte[2])
    if werte[3]:
        paket.ack = int(werte[3])
    if werte[4]:
        paket.dataofs = int(werte[4])
    if werte[5]:
        paket.reserved = int(werte[5])
    if werte[6]:
        paket.flags = int(werte[6])
    if werte[7]:
        paket.window = int(werte[6])
    if werte[8]:
        paket.urgptr = int(werte[7])
    if werte[9]:
        paket.options = werte[8]
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
            while i < int(werte[10]):
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
