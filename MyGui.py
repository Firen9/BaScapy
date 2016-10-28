from Tkinter import *
from scapy.all import IP,send,TCP
import ScapyCaller

fields = 'IP', 'DPort', 'SPort', 'ACK', 'dataofs', 'reserved', 'flags', 'window', 'urgptr', 'options','Fuzzing Anzahl'

def fetch(entries):
   eingabe=[]

   for entry in entries:
      eingabe.append(entry[1].get())
     # print(entry[1].get())

   ScapyCaller.createPaket(eingabe, fuzz.get())




def makeform(root, fields):
   entries = []
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=15, text=field, anchor='w')
      ent = Entry(row)
      row.pack(side=TOP, fill=X, padx=5, pady=5)
      lab.pack(side=LEFT)
      ent.pack(side=RIGHT, expand=YES, fill=X)
      entries.append((field, ent))
   return entries

def answerWindow(sendPaket,answerPaket):
    guitop = Toplevel()
    guitop.title("Gesendetes und empfangenes Paket")
    Label(guitop,text="Gesendete Paket").grid(row=0,column=0)
    Label(guitop, text="Empfanges Paket").grid(row=0,column=1)
    tSend=Text(guitop)
    tAnswer=Text(guitop)
    tSend.insert(END,sendPaket)
    tAnswer.insert(END,answerPaket)

    tSend.grid(row=1,column=0)
    tAnswer.grid(row=1,column=1)

def fuzzingWindow(sFuzz,aFuzz):
    guiFuzz = Toplevel()
    guiFuzz.title("Fuzzing Pakete")
    guiFuzz.geometry('120x125')

    frameListbox = Frame(master=guiFuzz)
    frameListbox.place(x=5,y=5,width=110, height=80)

    frameRelease = Frame(master=guiFuzz)
    frameRelease.place(x=5,y=90,width=110, height=30)

    listboxName = Listbox(master=guiFuzz, selectmode='browse')
    i=0
    asPaket=[]
    while i < len(aFuzz):
        listboxName.insert('end',aFuzz[i])
        i+=1

    listboxName.place(x=5,y=5,width=80, height=70)
    listboxName.bin('<<ListboxSelect>>')

    listSelect = listboxName.curselection()
    listSelect = listSelect[0]

    labelText=Label(master=frameRelease)
    labelText.config(text='Gesendet:\n' + sFuzz[0] + '\n' + 'Empfangen:\n' + aFuzz[0])
    labelText.place(x=5,y=5,width=100,height=20)





if __name__ == '__main__':
   root = Tk()
   root.title("StartScreen")
   ents = makeform(root, fields)
   root.bind('<Return>', (lambda event, e=ents: fetch(e)))

   fuzz=IntVar()
   Checkbutton(root,text="Fuzzing", variable=fuzz).pack(side=LEFT)

   b1 = Button(root, text='Verbinden', command=(lambda e=ents: fetch(e)))
   b1.pack(side=LEFT, padx=5, pady=5)

   b2 = Button(root, text='Quit', command=root.quit)
   b2.pack(side=LEFT, padx=6, pady=6)
   root.mainloop()
