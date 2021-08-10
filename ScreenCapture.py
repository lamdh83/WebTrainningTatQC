
import pyautogui
import cv2
#1920 x 1080

def screenCapture(name='screencapture'):
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(f'screencapture\{name}.png')

# img = cv2.imread('screencapture\screencapture.png')
# frameWidth = 1920
# framHeight = 1080
#
#
# img = cv2.resize(img,(frameWidth,framHeight))
#
#
# cv2.imshow('screen', img)
# cv2.waitKey(0)


if __name__ == '__main__':
    screenCapture()

