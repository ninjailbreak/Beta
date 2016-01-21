'''
 * @file CD_Eject.py
 * @brief close and open the cd Tray
 *
 * log
 * -----------
 * version 1.4 by ninjailbreak, 21.1.16
 * version 1.3 by ninjailbreak, 18.1.16
 * version 1.2 by ninjailbreak, 16.1.16
 * version 1.1 by ninjailbreak, 16.1.16
 * version 1.0 by ninjailbreak, 15.1.16
'''

from ctypes import windll
from os import system
from time import *
def menu1():
    windll.WINMM.mciSendStringW(u"set cdaudio door open", None, 0 , None)
def menu2():
    windll.WINMM.mciSendStringW(u"set cdaudio door closed", None, 0 , None)

from Tkinter import *
root = Tk()
frame = Frame(root)
frame.pack()
root.wm_title("CD Eject")
bottomframe = Frame(root)
bottomframe.pack(side = BOTTOM)

firstB = Button(bottomframe, text = "Open",fg = "red", command = menu1)
firstB.pack(side = LEFT)

label1 = Label(frame, text = "Welcome to CD Eject!")
label1.pack(side = TOP)

label2 = Label(frame, text = "")
label2.pack(side = TOP)

secondB = Button(bottomframe, text = "Close", fg = "blue" ,command = menu2)
secondB.pack(side = LEFT)

thirdB = Button(bottomframe, text = "Quit", fg = "black" , command = frame.quit)
thirdB.pack(side = BOTTOM)

root.mainloop()
