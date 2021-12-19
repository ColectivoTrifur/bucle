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
        self.out_video_name = "face_"+self.video_name
        self.out_video_path = self.output_path+self.out_video_name+'/'

    def write_output(self, frames):
        print("por escribir el video")
        if not os.path.exists(self.out_video_path):
            os.makedirs(self.out_video_path)
        i = 0
        video_identifier = self.out_video_path+'face_'+self.video_name+'_'
        for frame in tqdm(frames):
            digits = len(str(len(frames)))
            im = Image.fromarray(frame)
            frame_id=str(i)
            frame_id = frame_id.zfill(digits) 
            path = video_identifier +frame_id+'.png'
            im.save(path)
            i+=1
        print(">Finished work!")
        return len(frames)

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
                num_frames = self.write_output(frames)
                cv2.destroyAllWindows()
                return num_frames
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
