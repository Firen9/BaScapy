from Tkinter import *
from scapy.all import IP,send,TCP
import ScapyCaller

fields = 'IP', 'DPort', 'SPort', 'ACK', 'dataofs', 'reserved', 'flags', 'window', 'urgptr', 'options','Fuzzing Anzahl'

def fetch(entries):
   input=[]

   for entry in entries:
      input.append(entry[1].get())
     # print(entry[1].get())

   ScapyCaller.createPaket(input, fuzz.get())




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
    guitop.geometry('570x480')
    Label(guitop,text="Gesendete Paket").place(x=1,y=1)
    Label(guitop, text="Empfanges Paket").place(x=285,y=1)
    tSend=Text(guitop)
    tAnswer=Text(guitop)
    tSend.insert(END,sendPaket)
    tAnswer.insert(END,answerPaket)

    tSend.place(x=1,y=20,width=250, height=450)
    tAnswer.place(x=285,y=20, width=250, height=450)

    # Scroolbar
    sScroll = Scrollbar(master=guitop, orient='vertical')
    sScroll.place(x=260, y=20, width=15, height=450)
    tSend.config(yscrollcommand=sScroll.set)
    sScroll.config(command=tSend.yview)

    aScroll = Scrollbar(master=guitop, orient='vertical')
    aScroll.place(x=545, y=20, width=15, height=450)
    tAnswer.config(yscrollcommand=aScroll.set)
    aScroll.config(command=tAnswer.yview)

def onClick(event):
    # Feldauswahl
    widget=event.widget
    listSelect = widget.curselection()
    itemSelect = listSelect[0]
    paketSelect = widget.get(itemSelect)

    guiFuzz = Toplevel()
    guiFuzz.title("Fuzzing Pakete")
    guiFuzz.geometry('300x500')
    frameRelease = Frame(master=guiFuzz)
    frameRelease.place(x=5, y=5, width=300, height=500)

    tFuzzing=Text(frameRelease)
    tFuzzing.insert(END,paketSelect)
    tFuzzing.place(x=1, y=1, width=250, height=450)

    #Scroolbar
    yScroll = Scrollbar(master=guiFuzz, orient='vertical')
    yScroll.place(x=260, y=5, width=15,height=450)
    tFuzzing.config(yscrollcommand=yScroll.set)
    yScroll.config(command=tFuzzing.yview)

def fuzzingWindow(sFuzz,aFuzz):
    guiFuzz = Toplevel()
    guiFuzz.title("Fuzzing Pakete")
    guiFuzz.geometry('230x320')

    frameListbox = Frame(master=guiFuzz)
    frameListbox.place(x=1,y=1,width=190, height=290)

    listboxName = Listbox(master=guiFuzz, selectmode='browse')

    i=0
    asPaket=[]
    while i < len(aFuzz):
        asPaket.append('Empfangen:\n' + aFuzz[i] + '\n'+'Gesendet:\n' + sFuzz[i] + '\n')
        listboxName.insert('end',asPaket[i])
        i+=1

    listboxName.place(x=5,y=5,width=190, height=290)
    listboxName.bind("<Double-Button-1>", onClick)

    #Scroolbar
    yScroll = Scrollbar(master=guiFuzz, orient='vertical')
    yScroll.place(x=200,y=5, width=15,height=290)
    listboxName.config(yscrollcommand=yScroll.set)
    yScroll.config(command=listboxName.yview)

    xScroll = Scrollbar(master=guiFuzz,orient='horizontal')
    xScroll.place(x=5,y=300,width=190, height=15)
    listboxName.config(xscrollcommand=xScroll.set)
    xScroll.config(command=listboxName.xview)



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
