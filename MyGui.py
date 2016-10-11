from Tkinter import *
from scapy.all import IP,send,TCP
import ScapyCaller

fields = 'IP', 'DPort', 'SPort', 'ACK', 'dataofs', 'reserved', 'flags', 'window', 'urgptr', 'options','test'

def fetch(entries):
   eingabe=[]

   for entry in entries:
      eingabe.append(entry[1].get())
     # print(entry[1].get())

   ScapyCaller.createPacket(eingabe,fuzz)




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

if __name__ == '__main__':
   root = Tk()
   root.title("StartScreen")
   ents = makeform(root, fields)
   root.bind('<Return>', (lambda event, e=ents: fetch(e)))

   fuzz = BooleanVar()
   Checkbutton(root,text="Fuzzing", variable=fuzz).pack(side=LEFT)

   b1 = Button(root, text='Verbinden', command=(lambda e=ents: fetch(e)))
   b1.pack(side=LEFT, padx=5, pady=5)

   b2 = Button(root, text='Quit', command=root.quit)
   b2.pack(side=LEFT, padx=6, pady=6)
   root.mainloop()
