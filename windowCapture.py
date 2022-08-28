import numpy as np
import cv2, pyautogui, win32gui

class WindowCapture:
    def __init__(self,window_name,capture_rate):
        self.window_name = window_name
        self.frame=self.screenshot()


    def screenshot(self):
        hwnd = win32gui.FindWindow(None, self.window_name)
        if not hwnd:
            raise Exception('Window not found: ' + self.window_name)

        left, top, right, bot = win32gui.GetClientRect(hwnd)
        x, y = win32gui.ClientToScreen(hwnd, (left, top))

        return cv2.cvtColor(
            np.asarray(
                pyautogui.screenshot(
                    region=(x, y,
                            *win32gui.ClientToScreen(hwnd, (right - x, bot - y))))), cv2.COLOR_RGB2BGR)


    def fanScreen(self):
        hwnd = win32gui.FindWindow(None, self.window_name)
        if not hwnd:
            raise Exception('Window not found: ' + self.window_name)

        left, top, right, bot = win32gui.GetClientRect(hwnd)
        x, y = win32gui.ClientToScreen(hwnd, (left, top))

        return cv2.cvtColor(
            np.asarray(
                pyautogui.screenshot(
                    region=(x+(right*200/465), y+(bot*360/800),
                            right*110/465, bot*300/800))), cv2.COLOR_RGB2BGR)