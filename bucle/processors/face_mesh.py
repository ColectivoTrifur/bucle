import cv2
from cvzone.FaceMeshModule import FaceMeshDetector
from PIL import Image
from tqdm import tqdm
import os

class VideoFaceMesh:
    def __init__(self,*, video_name, video_path, output_path):
        self.cap = cv2.VideoCapture(video_path)
        self.detector = FaceMeshDetector()
        self.output_path = output_path
        self.video_name = video_name
        self.out_video_name = "mesh_"+self.video_name
        self.out_video_path = self.output_path+self.out_video_name+'/'

    def write_output(self, frames):
        print("por escribir el video")
        if not os.path.exists(self.out_video_path):
            os.makedirs(self.out_video_path)
        i = 0
        video_identifier = self.out_video_path+'mesh_'+self.video_name+'_'
        for frame in tqdm(frames):
            digits = len(str(len(frames)))
            im = Image.fromarray(frame)
            frame_id=str(i)
            frame_id = frame_id.zfill(digits) 
            path = video_identifier +frame_id+'.png'
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
            print("DOINGGGGGGGGG")
            success, img = self.cap.read()
            img = cv2.flip(img, 1)
            try:
                img, faces = self.detector.findFaceMesh(img)
                print(faces)
            except:
                #TODO:
                #detectar errores. dejar escrito en logs.
                self.write_output(frames)
                cv2.destroyAllWindows()
                return
            if faces:
                # bboxInfo => "id","bbox","score","center"
                print(dir(faces))
                center = faces[0]["center"]
                cv2.circle(img, center, 5, (255, 0, 255), cv2.FILLED)
                confidence = str(faces[0]["score"][0])+"\n"
                with open(confidence_path,'a') as file:
                    file.write(confidence)
            
            cv2.imshow("Image", img)
            frames.append(img)
            cv2.waitKey(1)

