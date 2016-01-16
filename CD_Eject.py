'''
 * @file CD_Eject.py
 * @brief close and open the cd Tray
 *
 * log
 * -----------
 * version 1.1 by ninjailbreak, 16.1.16
 * version 1.0 by ninjailbreak, 15.1.16
'''

from ctypes import windll

windll.WINMM.mciSendStringW(u"set cdaudio door open", None, 0 , None)
