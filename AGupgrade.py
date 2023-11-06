import time
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
import os
import subprocess
import time


def call_bsl():
    global exit_program
    if not exit_program:
        p = subprocess.Popen("bsl.bat", shell=True)
        (out, err) = p.communicate()
        print(out)
        ecode = p.wait(15)
        print("Exit Code=", ecode)
        button.configure(text='>> Done! <<')
        exit_program = 1
    else:
        win.destroy()


win = Tk()
win.geometry('310x390')  # 390
win.title("KMI-FSS Relay Driver")

canvas = Canvas(win, bg="blue", height=310, width=310)
filename = PhotoImage(file="Logo.png")
background_label = Label(win, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
canvas.grid(column=0, row=0, sticky="n")

frame = Frame(win)
frame.grid(column=0, row=1, sticky="s")

label = Label(frame, text="Upgrading Amp Genie II \n to version 2.0.1")
label.grid(column=0, row=0, sticky="s")

button = Button(frame, text='Upgrade AmpGenie', command=call_bsl)
button.grid(column=0, row=1, sticky="s")
exit_program = 0

win.mainloop()


