import sys
import win32con, win32gui, win32api
import wx
import time

WINDOW_SIZE = (win32api.GetSystemMetrics(0),win32api.GetSystemMetrics(1))

def drawFrame():
    app = wx.App()
    frame = wx.Frame(parent=None, size=WINDOW_SIZE, style=wx.CLIP_CHILDREN | wx.STAY_ON_TOP)

    hwnd = frame.GetHandle()

    extendedStyleSettings = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
    win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, extendedStyleSettings | win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT)
    win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(0,0,0), 255, win32con.LWA_ALPHA)
    frame.SetTransparent(255)
    panel = wx.Panel(parent=frame, style=wx.CLIP_CHILDREN, size=WINDOW_SIZE)

    frame.Show()
    time.sleep(2)


drawFrame()
