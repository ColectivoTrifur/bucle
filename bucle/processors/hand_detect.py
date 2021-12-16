import cv2
from cvzone.HandTrackingModule import HandDetector

class VideoHandDetector:
    def __init__(self, *, video_name, video_path, output_path):
        self.cap = cv2.VideoCapture(video_path)
        self.detector = HandDetector(detectionCon=0.8)
        self.cap.set(3, 1280) #TODO: ver de sacar este número de forma dinámica
        self.cap.set(4, 720) #TODO: ver de sacar este número de forma dinámica
        self.output_path = output_path
        self.video_name = video_name


    def run(self):
        print(">Beginning work!")
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
            #TODO:
            #acumular img y en el break escribir a un archivo en OUTPUT_PATH
            cv2.waitKey(1)

