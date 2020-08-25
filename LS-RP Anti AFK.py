# -*- coding: utf-8 -*-

import pyautogui
import os
import time
import sys
from shutil import copyfile
from datetime import datetime

def now():
    return datetime.now().time()
def copy():
    copyfile(r'c:\users\temporary user\documents\gta san andreas user files\samp\chatlog.txt', r'c:\users\temporary user\documents\gta san andreas user files\samp\chatlogp.txt')
def remove():
    os.remove(r'c:\users\temporary user\documents\gta san andreas user files\samp\chatlogp.txt')
    print ("chatlog removed!")
def check():
    print ("check started at ", now())
    time.sleep(10)
    pyautogui.typewrite("t/admins")
    pyautogui.press('enter')
    copy()
    f = open(r'c:\users\temporary user\documents\gta san andreas user files\samp\chatlogp.txt','r')
    message = f.readlines()
    lastline = (list(message) [-2])
    if "There's no administrators online." in lastline:
        print (lastline)
        f.close()
        remove()
        pyautogui.typewrite("t/time")
        pyautogui.press('enter')
        pyautogui.keyDown('w')
        time.sleep(0.25)
        pyautogui.keyUp('w')
        pyautogui.keyDown('s')
        time.sleep(0.25)
        pyautogui.keyUp('s')
        return True
    else:
        print ("admin may be present...")
        f.close()
        remove()
        return False


while True:
    if check() or check():
        print ("done")
        time.sleep(1200)
    else:
        print ("quitting at ", now())
        pyautogui.typewrite("t/q")
        pyautogui.press('enter')
        sys.exit("successfully exited")