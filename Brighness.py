#!/usr/bin/python

from Tkinter import *
import commands

def buscar_video():
    status, output = commands.getstatusoutput('xrandr -q | grep " connected"')
    list =[]
    for char in output:
        if char != ' ':
            list.append(char)
        else:
            break
    video = ''.join(list)
    return video

master = Tk()

w = Scale(master, from_=10, to=100, orient=HORIZONTAL)
w.set(100)
w.config(borderwidth=9)
w.pack()

def change_brilho():

    value = w.get()
    video = buscar_video()

    #commands.getstatusoutput("xrandr --output {} --brightness {}".format(video, value/100.0))

    master.after(800, change_brilho)

master.after(800, change_brilho)
master.mainloop()
