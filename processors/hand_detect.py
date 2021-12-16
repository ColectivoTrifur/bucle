import cv2
from cvzone.HandTrackingModule import HandDetector
import random

class VideoHandDetector:
    def __init__(self, *, video_name, video_path, output_path):
        self.video_name = video_name
        self.cap = cv2.VideoCapture(video_path)
        self.detector = HandDetector(detectionCon=0.8)
        self.cap.set(3, 1280)
        self.cap.set(4, 720)
        self.output_path = output_path


    def run(self):
        print("Beginning work!")
        i=0
        while True:
            print(i)
            i+=1
            success, img = self.cap.read()
            img = cv2.flip(img, 1)
            try:
                img = self.detector.findHands(img)
            except:
                print("Finished work!")
                break
            lmList, _ = self.detector.findPosition(img)
            print(lmList)
            if lmList:

                # l,_,_ = detector.findDistance(8,12,img)
                l, _, _ = self.detector.findDistance(4, 8, img)
                print(l)
                with open(self.output_path+self.video_name+'_distance.csv','a') as file:
                    file.write(str(l)+"\n")
                cursor = lmList[8]
                print(cursor)
                with open(self.output_path+self.video_name+'_cursor.csv','a') as file:
                    file.write(str(cursor[0])+','+str(cursor[1])+"\n")
            cv2.imshow("Image", img)
            cv2.waitKey(1)

