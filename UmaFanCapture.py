import numpy as np
import cv2, pyautogui, win32gui

class UmaFanCapture:
    def __init__(self):
        self.frame=self.WindowCapture()
        
    def WindowCapture(self):
        wintitle = win32gui.GetWindowText(win32gui.GetForegroundWindow())
        hwnd = win32gui.FindWindow(None, wintitle)

        left, top, right, bot = win32gui.GetClientRect(hwnd)
        x, y = win32gui.ClientToScreen(hwnd, (left, top))

        screen_ = pyautogui.screenshot(region=(x+(right*200/465), y+(bot*360/800),right*110/465, bot*300/800))
        try:
            screen_ = cv2.cvtColor(np.asarray(screen_), cv2.COLOR_RGB2BGR)
        except:
            screen_ = img = np.zeros((512,512,3), np.uint8)
        
        return screen_
        
def text2list(text):
    blist = []
    text = text.split('\n')

    for a in text:
        if ',' in a:
            blist.append(a)

        for b in range(len(blist)):
            if blist[b][::-1].find(',') ==4:
                blist[b] = blist[b][:-1]
            blist[b] = blist[b].replace(",","")

    return blist

def list2clipboard(list):
    clip = ""
    for a in list:
        clip += a + "\n"

    return clip[:-1]