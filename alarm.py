from tkinter import *
from tkinter import messagebox
import time
import datetime
import threading
from pygame import mixer

root= Tk()
root.title("Alarm Clock")
root.geometry("600x400")
root.configure(bg="light blue")

alarmtime = StringVar()
msgi = StringVar()

head =Label(root,text="ALARM CLOCK",font=("impack 16 bold"),bg="black", fg="white")
head.grid(row=0,column=1,columnspan=5, pady=20)

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

alpp = PhotoImage(file='Alarm.png')

alp = Label(root,image=alpp)
alp.grid(rowspan=4,column=0)

inputt = Label(root,text="Set time:",font=('comic sans',18),bg="dark blue",fg= "white")
inputt.grid(row=1,column=1)

altime = Entry(root,textvariable=alarmtime,font=('comic sans',18),bg="light yellow",fg= "black",width=8)
altime.grid(row=1,column=2)

msg = Label(root,text="Message", font=('comic sans',18))
msg.grid(row=2,column=1,columnspan=2)

msginput = Entry(root,textvariable=msgi,font=('comic sans',18))
msginput.grid(row=3,column=1,columnspan=2,padx=8)

submit = Button(root,text="Set Alarm", font=('comic sans',18),bg="green",fg= "white",command=ala)
submit.grid(row=4,column=1,columnspan=2)

root.mainloop()
