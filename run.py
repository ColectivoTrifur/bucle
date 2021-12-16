import os
from constants import RAW_DIR, OUTPUT_DIR
from processors.hand_detect import VideoHandDetector
from processors.face_detect import VideoFaceDetector

# en un futuro esto será un worker
def process():
    #TODO: reemplazar por sacar de una cola de redis
    for video in os.listdir(RAW_DIR):
        print("[*] Processing video ",video)
        video_name = video.split(".")[0]
        print("[*] Processing hands")
        hand_detect_process = VideoHandDetector(video_name = video_name, video_path=RAW_DIR+video, output_path=OUTPUT_DIR)
        hand_detect_process.run()
        print("[*] Processing faces")
        face_detect_process = VideoFaceDetector(video_name = video_name, video_path=RAW_DIR+video, output_path=OUTPUT_DIR)
        face_detect_process.run()

process()
#visualize()
