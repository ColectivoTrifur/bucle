import cv2
from cvzone.HandTrackingModule import HandDetector
import random

cap = cv2.VideoCapture('../videos/rob.mp4')

cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon=0.8)

magenta = (255, 0, 255)
colorR = magenta
cx, cy = 100, 100
width, height = 100, 100
offset = 0


while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    try:
        img = detector.findHands(img)
    except:
        break
    lmList, _ = detector.findPosition(img)
    if lmList:

        # l,_,_ = detector.findDistance(8,12,img)
        l, _, _ = detector.findDistance(4, 8, img)
        print(l)
        with open('./outputs/distance.csv','a') as file:
            file.write(str(l)+"\n")
        cursor = lmList[8]
        print(cursor)
        with open('./outputs/cursor.csv','a') as file:
            file.write(str(cursor[0])+','+str(cursor[1])+"\n")
    cv2.imshow("Image", img)
    cv2.waitKey(1)

