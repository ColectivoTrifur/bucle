import cv2
from cvzone.FaceDetectionModule import FaceDetector
import random


cap = cv2.VideoCapture('../videos/rob.mp4')

cap.set(3, 1280)
cap.set(4, 720)
face_detector = FaceDetector()

magenta = (255, 0, 255)
colorR = magenta
cx, cy = 100, 100
width, height = 100, 100
offset = 0

while True:

    success, img = cap.read()
    img = cv2.flip(img, 1)
    try:
        img,bboxs = face_detector.findFaces(img)
    except:
        break
    if bboxs:
        # bboxInfo => "id","bbox","score","center"
        center = bboxs[0]["center"]
        cv2.circle(img, center, 5, (255, 0, 255), cv2.FILLED)
        confidence = str(bboxs[0]["score"][0])+"\n"
        with open('./outputs/face_rob.csv','a') as file:
            file.write(confidence)
        print(f'Detected {confidence}')
    
    cv2.imshow("Image", img)
    cv2.waitKey(1)
