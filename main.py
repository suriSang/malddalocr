import UmaFanCapture
import time, threading, keyboard, clipboard
import cv2, pytesseract
pytesseract.pytesseract.tesseract_cmd = R'C:\Program Files\Tesseract-OCR\tesseract.exe'

member_list = []
Running = True
previousTime = 0

FRAME_RATE = 60
sampleTime = 1/FRAME_RATE

time.sleep(1)
capture = UmaFanCapture.UmaFanCapture()


def keyboard_input():
    global Running, member_list
    while Running:
        key = keyboard.read_key()

        if key == "space":
            text = pytesseract.image_to_string(frame)
            blist = UmaFanCapture.text2list(text)
            print(blist)
            member_list.extend(blist)

        if key == "z":
            print(member_list)
            time.sleep(0.5)

        if key == "x":
            if len(member_list) != 0:
                member_list = member_list[:-1]
            print(member_list)
            time.sleep(0.5)

        if key == "c":
            clipboard.copy(UmaFanCapture.list2clipboard(member_list))
            Running = False

t = threading.Thread(target=keyboard_input)
t.start()

while Running:
    currentTime = time.perf_counter()
    if currentTime - previousTime >= sampleTime:
        frame = capture.WindowCapture()
        cv2.imshow("frame1",frame)
        cv2.waitKey(1) & 0xFF
        if cv2.waitKey(1) & 0xFF == ord('c'):
            break

        previousTime = currentTime
t.join()