'''
 * @file CD_Eject.py
 * @brief close and open the cd Tray
 *
 * log
 * -----------
 * version 1.3 by ninjailbreak, 18.1.16
 * version 1.2 by ninjailbreak, 16.1.16
 * version 1.1 by ninjailbreak, 16.1.16
 * version 1.0 by ninjailbreak, 15.1.16
'''

from ctypes import windll
from os import system
from time import *
def menu():
    system("cls")
    print "Welcome to CD Eject!"
    ans = input("""So what are you want to do?
    1. Open
    2. Close
    3. Exit
    """)
    print
    print
    if ans == 3:
        system("cls")
        print "Good Bye!"
        exit()
    elif ans == 1:
        print "Open Now!"
        windll.WINMM.mciSendStringW(u"set cdaudio door open", None, 0 , None)
    elif ans == 2:
        print "Close Now!"
        windll.WINMM.mciSendStringW(u"set cdaudio door closed", None, 0 , None)
    sleep(0.2)
system("color A")
while True:
    menu()
