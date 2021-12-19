import cv2
from cvzone.HandTrackingModule import HandDetector
import os
from PIL import Image

class VideoHandDetector:
    def __init__(self, *, video_name, video_path, output_path):
        self.cap = cv2.VideoCapture(video_path)
        self.detector = HandDetector(detectionCon=0.8)
        self.cap.set(3, 1280) #TODO: ver de sacar este número de forma dinámica
        self.cap.set(4, 720) #TODO: ver de sacar este número de forma dinámica
        self.output_path = output_path
        self.video_name = video_name
        self.out_video_path = self.output_path+self.video_name+'_hand/'


    def run(self):
        video_output=[]
        print(">Beginning work!")
        if not os.path.exists(self.out_video_path):
            os.makedirs(self.out_video_path)
        distance_path = self.output_path+self.video_name+'_distance.csv'
        cursor_path = self.output_path+self.video_name+'_cursor.csv'

        #TODO:
        #detectar si archivo ya existe. en cuyo caso, agregarle un index
        while True:
            success, img = self.cap.read()
            img = cv2.flip(img, 1)
            try:
                img = self.detector.findHands(img)
            except:
                #TODO:
                #detectar errores. dejar escrito en logs.
                print("por escribir el video")
                i = 0
                for frame in video_output:
                    print(i)
                    im = Image.fromarray(frame)
                    path = self.out_video_path+'hand_'+self.video_name+'_'+str(i)+'.png'
                    print(path)
                    im.save(path)
                    i+=1
                print(">Finished work!")
                break
            lmList, _ = self.detector.findPosition(img)
            if lmList:

                # l,_,_ = detector.findDistance(8,12,img)
                l, _, _ = self.detector.findDistance(4, 8, img)
                with open(distance_path,'a') as file:
                    file.write(str(l)+"\n")
                cursor = lmList[8]
                with open(cursor_path,'a') as file:
                    file.write(str(cursor[0])+','+str(cursor[1])+"\n")
            cv2.imshow("Image", img)
            video_output.append(img)
            #TODO:
            #acumular img y en el break escribir a un archivo en OUTPUT_PATH
            cv2.waitKey(1)

