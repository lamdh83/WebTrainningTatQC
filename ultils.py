import cv2
import pyautogui
import autopy
import time


import  numpy as np

from datetime import datetime

now = datetime.now()

wCam, hCam = 640, 480
cap = cv2.VideoCapture('your_video.avi')
cap.set(3, wCam)
cap.set(4, hCam)

# detector = htm.handDetector(detectionCon=0.75)
#
# tipIds = [4, 8, 12, 16, 20]
#
# pytesseract.pytesseract.tesseract_cmd = 'D:\\Tesseract-OCR\\tesseract.exe'

def CatHinh(img, scale=0.2):

    h,w,c = img.shape
    x = int(w*scale)
    y = int(h*scale)
    imgCrop = img[h-y:h, w-x:w]
    # print(f'h{h} / w {w} / c {c}')
    return w,h,w - x, h - y,imgCrop

def CatHinh1(img, scale=2):

    h,w,c = img.shape
    x = int(w/scale)
    y = int(h*2/3)
    imgCrop = img[y:y + 100, x:x + 300]
    # print(f'h{y} / w {x} ')
    return w,h,x, y,imgCrop

def screenCapture(name='screencapture'):
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(f'screencapture\{name}.png')



def empty(a):
    pass



def TaTQQDuoi(wScr, hScr, wImg, hImg):
    # print(f'TaTQQDuoi {wScr}/{hScr} / {wImg} / {hImg}')
    scaleX = wImg / wScr
    scaleY = hImg / hScr
    x3 = 1800 / scaleX
    y3 = 936 / scaleY
    # print(f'tao do bam QQ Duoi {x3}/{y3}')
    autopy.mouse.move(x3, y3)
    autopy.mouse.click()
    time.sleep(5)

def TatQQTren(wScr, hScr, wImg, hImg):
    # print('TatQQTren')
    scaleX = wImg / wScr
    scaleY = hImg / hScr
    x3 = 1109 / scaleX
    y3 = 737 / scaleY
    # print(f'tao do bam {x3}/{y3}')
    autopy.mouse.move(x3, y3)
    autopy.mouse.click()
    time.sleep(5)

def TatQQHDuoi(wScr, hScr, wImg, hImg):
    # print(f'TaTQQ Hinh Duoi {wScr}/{hScr} / {wImg} / {hImg}')
    scaleX = wImg / wScr
    scaleY = hImg / hScr
    x3 = 1399 / scaleX
    y3 = 890 / scaleY
    # print(f'tao do bam QQ Hinh duoi {x3}/{y3}')
    autopy.mouse.move(x3, y3)
    autopy.mouse.click()
    time.sleep(5)

def TatQQHTren(wScr, hScr, wImg, hImg):
    # print('TatQQHTren')
    scaleX = wImg / wScr
    scaleY = hImg / hScr
    x3 = 1121 / scaleX
    y3 = 694 / scaleY
    # print(f'tao do bam {x3}/{y3}')
    autopy.mouse.move(x3, y3)
    autopy.mouse.click()
    time.sleep(5)


# cv2.namedWindow('Parameters')
# cv2.resizeWindow('Parameters', 640, 240)
# #cv2.createTrackbar('Threshold1','Parameters', 150, 255, empty)
# #cv2.createTrackbar('Threshold2','Parameters', 255, 255, empty)
# cv2.createTrackbar('Threshold1','Parameters', 23, 255, empty) # 100
# cv2.createTrackbar('Threshold2','Parameters', 20, 255, empty) # 20
# cv2.createTrackbar('Area','Parameters', 5000, 30000, empty) # 10000

if __name__=="__main__":
    while True:
        # success, img = cap.read()
        # countFinger(img)
        img = cv2.imread('QqHinh//3.PNG')
