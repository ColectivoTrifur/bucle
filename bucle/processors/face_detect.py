import cv2
from cvzone.FaceDetectionModule import FaceDetector
from PIL import Image
from tqdm import tqdm
import os

class VideoFaceDetector:
    def __init__(self,*, video_name, video_path, output_path):
        self.cap = cv2.VideoCapture(video_path)
        self.detector = FaceDetector()
        self.output_path = output_path
        self.video_name = video_name
        self.out_video_path = self.output_path+self.video_name+'_face/'

    def write_output(self, video_output):
        print("por escribir el video")
        if not os.path.exists(self.out_video_path):
            os.makedirs(self.out_video_path)
        i = 0
        for frame in tqdm(video_output):
            im = Image.fromarray(frame)
            path = self.out_video_path+'hand_'+self.video_name+'_'+str(i)+'.png'
            im.save(path)
            i+=1
        print(">Finished work!")

    def run(self):
        print(">Beginning work!")
        frames=[]
        confidence_path = self.output_path+self.video_name+'_confidence.csv'

        #TODO:
        #detectar si archivo ya existe. en cuyo caso, agregarle un index
        while True:

            success, img = self.cap.read()
            img = cv2.flip(img, 1)
            try:
                img,bboxs = self.detector.findFaces(img)
            except:
                self.write_output(frames)
                break
            if bboxs:
                # bboxInfo => "id","bbox","score","center"
                center = bboxs[0]["center"]
                cv2.circle(img, center, 5, (255, 0, 255), cv2.FILLED)
                confidence = str(bboxs[0]["score"][0])+"\n"
                with open(confidence_path,'a') as file:
                    file.write(confidence)
            
            cv2.imshow("Image", img)
            frames.append(img)
            cv2.waitKey(1)
