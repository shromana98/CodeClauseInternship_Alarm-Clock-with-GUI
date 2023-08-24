from tkinter import *
from tkinter import messagebox
import time
import datetime
import threading
from pygame import mixer

root= Tk()
root.title("Alarm Clock")
root.geometry("550x350")

alarmtime = StringVar()
msgi = StringVar()

head =Label(root,text="ALARM CLOCK",font=('comic sans',22))
head.grid(row=0,columnspan=3, pady=10)

mixer.init()

def ala():
    a = alarmtime.get()
    AlarmT = a
    CurrentTime = time.strftime("%H:%M")

    while AlarmT != CurrentTime:
        CurrentTime = time.strftime("%H:%M")
    if AlarmT == CurrentTime:
        mixer.music.load('alarm-tone.mp3')
        mixer.music.play()
        msg = messagebox.showinfo('Info',f'{msgi.get()}')
        if msg == 'ok':
            mixer.music.stop()

alpp = PhotoImage(file='al.png')

alp = Label(root,image=alpp)
alp.grid(rowspan=4,column=0)

inputt = Label(root,text="Input time",font=('comic sans',18))
inputt.grid(row=1,column=1)

altime = Entry(root,textvariable=alarmtime,font=('comic sans',18),width=6)
altime.grid(row=1,column=2)

msg = Label(root,text="Message", font=('comic sans',18))
msg.grid(row=2,column=1,columnspan=2)

msginput = Entry(root,textvariable=msgi,font=('comic sans',18))
msginput.grid(row=3,column=1,columnspan=2)

submit = Button(root,text="Set Alarm", font=('comic sans',18),command=ala)
submit.grid(row=4,column=1,columnspan=2)

root.mainloop()
