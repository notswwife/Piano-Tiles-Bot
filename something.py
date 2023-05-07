import win32api
import win32con
from pyautogui import *
import pyautogui
import time
import keyboard
import random

#Title 1 Position: X:  603 Y:  474 RGB: (154, 159, 230)
#Title 2 Position: X:  696 Y:  474 RGB: (174, 178, 234) 
#Title 3 Position: X:  770 Y:  474 RGB: (159, 163, 230)
#Title 4 Position: X:  858 Y:  474 RGB: (  0,   0,   0)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.05)  # reduce delay to 1 millisecond
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


while keyboard.is_pressed('q') == False:

    if pyautogui.pixel(603, 474) [0] == 0:
        click(603, 474)
    if pyautogui.pixel(696, 474) [0] == 0:
        click(696, 474)
    if pyautogui.pixel(770, 474) [0] == 0:
        click(770, 474)
    if pyautogui.pixel(858, 474) [0] == 0:
        click(858, 474)

