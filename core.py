import win32gui
global hand
hwnd = 0

def findWindow_runelite(Name):
    global hwnd
    hwnd = win32gui.FindWindow(None, "RuneLite - " + Name)
    print('findwindow:', hwnd)
    win32gui.SetActiveWindow(hwnd)

    win32gui.MoveWindow(hwnd, 0, 0, 865, 830, True)

findWindow_runelite('PaulFoster')