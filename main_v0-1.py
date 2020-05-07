from tkinter import filedialog
from tkinter import *
from pygame import mixer  # pip install pygame

anzahlTitel = 3  # anzah zu wählender titel als default wertListeDateien = []

ListeDateien = []
ListeNamen = []

ListebuttonPlay = []
ListebuttonName = []
ListebuttonDatei = []

try:
    Gelesenedatei = open("saveFiles.txt")
    i = 0
    for line in Gelesenedatei:
        if i == 0:
            anzahlTitel = (line.rstrip())
            for nr in range(int(anzahlTitel)):
                ListeDateien.append("empty field: " + str(nr + 1))

        else:
            ListeDateien[i - 1] = line.rstrip()
        i = i + 1

    Gelesenedatei.close()


except:

    for i in range(anzahlTitel):
        ListeDateien.append("Datei " + str(i + 1))

try:
    Gelesenedatei = open("saveNames.txt")
    i = 0
    for nr in range(int(anzahlTitel)):
        ListeNamen.append("Song: " + str(nr + 1))
    for line in Gelesenedatei:
        ListeNamen[i] = line.rstrip()
        i = i + 1
    Gelesenedatei.close()


except:

    for i in range(anzahlTitel):
        ListeNamen.append("Song: " + str(i + 1))

mixer.init()


def aktion(i):
    global mixer
    print(ListeDateien[i])
    print(ListeNamen[i])
    mixer.music.load(ListeDateien[i])
    mixer.music.play()


def getentry(text, field, A):

    ListeNamen[field] = text.get()
    ListebuttonName[field].config(text=ListeNamen[field])
    A.destroy()


def callback(x, stat):
    if stat:
        root.filname = filedialog.askopenfilename(initialdir="./", title="Select files",
                                                  filetypes=(("mp3 files", "*.mp3"), ("all", "*.*")))
        if root.filname != "":
            ListeDateien[x] = root.filname
            ListebuttonDatei[x].config(text=ListeDateien[x])

    else:

        Fill = Tk()
        L = Label(Fill, text="Name : ")
        # Name = StringVar()
        E = Entry(Fill, bd=5)
        B = Button(Fill, text="Speichern.", command=(lambda y=E, z=x, A=Fill: getentry(y, z, A)))
        L.pack(side=LEFT)
        E.pack()
        B.pack()
        Fill.mainloop()


def call_exit():
    global anzahlTitel
    Output = open("saveFiles.txt", "w")
    Output.write(str(anzahlTitel) + "\n")
    for line in ListeDateien:
        Output.write(line + "\n")
    Output.close()
    Output = open("saveNames.txt", "w")
    for line in ListeNamen:
        Output.write(line + "\n")
    Output.close()
    exit(0)


def stop():
    global mixer
    mixer.music.stop()


root = Tk()

# w,h =


for i in range(len(ListeDateien)):
    ListebuttonPlay.append("buttonPlay" + str(i))
    ListebuttonPlay[i] = Button(root, text="  Play  ", command=(lambda x=i: aktion(x)))
    ListebuttonPlay[i].grid(row=(0 + i), column=0)

    ListebuttonName.append("buttonName" + str(i))
    ListebuttonName[i] = Button(root, text=("  " + ListeNamen[i]), command=(lambda x=i: callback(x, False)))
    ListebuttonName[i].grid(row=(0 + i), column=1)

    ListebuttonDatei.append("buttonDatei" + str(i))
    ListebuttonDatei[i] = Button(root, text=("  " + ListeDateien[i]), command=(lambda x=i: callback(x, True)))
    ListebuttonDatei[i].grid(row=(0 + i), column=2)

buttonSTOP = Button(root, text="Stop", fg="red", command=stop)
buttonSTOP.grid(row=(len(ListeDateien) + 2), column=0)

buttonExit = Button(root, text='Quit', command=call_exit)
buttonExit.grid(row=(len(ListeDateien) + 2), column=1)

root.mainloop()
