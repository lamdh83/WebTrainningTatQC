# cvzone 1.3.3
#tensorflow
import autopy as autopy
import cvzone
import cv2
from ScreenCapture import *
from catHinh import *
from ultils import *
from datetime import datetime

number = 0
num = 0
numChu = 0

wScr, hScr = autopy.screen.size()
wImg = 1920
hImg = 1080


cap = cv2.VideoCapture(0)
myClassifier = cvzone.Classifier('Mymodels//keras_model.h5','Mymodels//labels.txt')
fpsReader = cvzone.FPS()

if __name__ == '__main__':
    while True:

        # _, img = cap.read()
        screenCapture()
        img = cv2.imread('Screencapture//screencapture.png')
        w, h, imgHinh = CatButton(img)
        w, h, imgChu = CatButtonChu(img)

        # imgT = cv2.imread('QqHinh//2.png')
        # imgT = cv2.resize(imgT,(224,224))
        predictionHinh, indexHinh = myClassifier.getPrediction(imgHinh)
        predictionChu, indexChu = myClassifier.getPrediction(imgChu)
        # print(f'{predictionHinh[indexHinh]}')




        # print(predictionChu[indexChu])
        if predictionHinh[indexHinh] >= 0.99995:
            cv2.imwrite(f'Screencapture//Hinh_{predictionHinh[indexHinh]}_{number}.png', imgHinh)

            TatQQHDuoi(wScr, hScr, wImg, hImg)
            # print(f'num:{num}')
            # print(f'{predictionHinh[indexHinh]}')
            # num += 1
            # if num >= 2:
            #     cv2.imwrite(f'Screencapture//Hinh_{predictionHinh[indexHinh]}_{number}.png',imgHinh)
            #
            #     TatQQHDuoi(wScr, hScr, wImg, hImg)
            #     print(predictionHinh[indexHinh])
            #     num = 0

        if predictionChu[indexChu] >= 0.99999:
            cv2.imwrite(f'Screencapture//Chu_{predictionChu[indexChu]}_{number}.png', imgChu)

            TaTQQDuoi(wScr, hScr, wImg, hImg)
            # print(f'numChu {numChu}')
            # print(f' {predictionChu[indexChu]}')
            # numChu += 1
            # if numChu >= 2:
            #     cv2.imwrite(f'Screencapture//Chu_{predictionChu[indexChu]}_{ number}.png', imgChu)
            #
            #     TaTQQDuoi(wScr, hScr, wImg, hImg)
            #     print(predictionChu[indexChu])
            #     numChu = 0

        number += 1



        # print(f'HINH {predictionHinh}, {indexHinh}')
        # print(f'CHU {predictionChu}, {indexChu}')
        # # fps, img = fpsReader.update(img, pos=(20, 100))
        # cv2.imshow('HINH', imgHinh)
        # cv2.imshow('CHU', imgChu)
        # cv2.waitKey(1)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
