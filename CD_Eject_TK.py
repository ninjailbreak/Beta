
'''
* @file CD_Eject_TK.py
* @brief close and open the cd Tray with GUI
*
* log
* -----------
* version 1.0 by ninjailbreak, 21.1.16
'''
from os import system
from time import *
from Tkinter import *

class CD_Eject:
	
	def __init__(self,master):
		frame = Frame(master)
		frame.pack()

		root.wm_title("CD Eject")

		bottomframe = Frame(master)
		bottomframe.pack(side = BOTTOM)

		firstB = Button(bottomframe, text = "Open",fg = "red", command = self.open_OS)
		firstB.pack(side = LEFT)

		label1 = Label(frame, text = "        Welcome to CD Eject!        ")
		label1.pack(side = TOP)

		label2 = Label(frame, text = "")
		label2.pack(side = TOP)

		secondB = Button(bottomframe, text = "Close", fg = "blue" ,command = self.close_OS)
		secondB.pack(side = LEFT)

		thirdB = Button(bottomframe, text = "Quit", fg = "black" , command = frame.quit)
		thirdB.pack(side = BOTTOM)


	def open_cd(self,i):
		if i == 0:
		    system("eject cdrom")
		elif i == 1:
		    from ctypes import windll
		    windll.WINMM.mciSendStringW(u"set cdaudio door open", None, 0 , None)

	def close_cd(self,i):
		if i == 0:
		    system("eject -t cdrom")
		elif i == 1:
		    from ctypes import windll
		    windll.WINMM.mciSendStringW(u"set cdaudio door closed", None, 0 , None)

	def open_OS(self):
		self.open_cd(system("clear"))

	def close_OS(self):
		self.close_cd(system("clear"))


root = Tk()

CD = CD_Eject(root)

root.mainloop()
