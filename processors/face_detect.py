import cv2
from cvzone.FaceDetectionModule import FaceDetector

class VideoFaceDetector:
    def __init__(self,*, video_name, video_path, output_path):
        self.cap = cv2.VideoCapture(video_path)
        self.detector = FaceDetector()
        self.cap.set(3, 1280)
        self.cap.set(4, 720)
        self.output_path = output_path
        self.video_name = video_name

    def run(self):
        print(">Beginning work!")
        confidence_path = self.output_path+self.video_name+'_confidence.csv'

        #TODO:
        #detectar si archivo ya existe. en cuyo caso, agregarle un index
        while True:

            success, img = self.cap.read()
            img = cv2.flip(img, 1)
            try:
                img,bboxs = self.detector.findFaces(img)
            except:
                print(">Finished work!")
                break
            if bboxs:
                # bboxInfo => "id","bbox","score","center"
                center = bboxs[0]["center"]
                cv2.circle(img, center, 5, (255, 0, 255), cv2.FILLED)
                confidence = str(bboxs[0]["score"][0])+"\n"
                with open(confidence_path,'a') as file:
                    file.write(confidence)
            
            cv2.imshow("Image", img)
            cv2.waitKey(1)
