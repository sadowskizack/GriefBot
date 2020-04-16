import sys
import wx
import win32con
import win32gui
import win32api
import wx
import time
from playsound import playsound
import socket

HOST = "irc.twitch.tv"
NICK = "dafarmguy"
PORT = 6667
PASS = #""

def send_message(message):
    s.send(bytes("PRIVMSG #" + NICK + " :" + message + "\r\n", "UTF-8"))

# commented out because it's annoying, as intended
def DONO():
    playsound("DONO-INTRO.mp3")

WINDOW_SIZE = (win32api.GetSystemMetrics(0),win32api.GetSystemMetrics(1))

def drawFrame(dono = False):
    if dono:
        DONO()
    app = wx.App()
    frame = wx.Frame(parent=None, size=WINDOW_SIZE, style=wx.CLIP_CHILDREN | wx.STAY_ON_TOP)

    hwnd = frame.GetHandle()

    extendedStyleSettings = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)

    win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, extendedStyleSettings | win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT)

    win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(255,255,255), 255, win32con.LWA_ALPHA)

    frame.SetTransparent(0)

    panel = wx.Panel(parent=frame, style=wx.CLIP_CHILDREN, size=WINDOW_SIZE)

    frame.Show()

    for i in range(1,25):
        frame.SetTransparent(i * 10.2000002)

        panel = wx.Panel(parent=frame, style=wx.CLIP_CHILDREN, size=WINDOW_SIZE)
        frame.Show()
        time.sleep(.1)
    time.sleep(2)

    win32gui.DestroyWindow(hwnd)

s = socket.socket()
s.connect((HOST, PORT))
s.send(bytes("PASS " + PASS + "\r\n", "UTF-8"))

s.send(bytes("NICK " + NICK + "\r\n", "UTF-8"))

s.send(bytes("JOIN #CaptainValerion \r\n", "UTF-8"))


while True:
    line = str(s.recv(1024))
    if "End of /NAMES list" in line:
        break

while True:
    for line in str(s.recv(1024)).split('\\r\\n'):
        parts = line.split(':')
        if len(parts) < 3:
            continue

        if "QUIT" not in parts[1] and "JOIN" not in parts[1] and "PART" not in parts[1]:
            message = parts[2][:len(parts[2])]

        usernamesplit = parts[1].split("!")
        username = usernamesplit[0]

        print(username + ": " + message)

        if username.upper() == "CAPTAINVALERION":
            send_message("Fuck you, " + username)

        if message.upper() == "LIGHTS OUT":
            send_message("NIGHT NIGHT, " + username)
            drawFrame()


