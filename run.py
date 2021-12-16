import os
from constants import RAW_DIR, OUTPUT_DIR
from processors.hand_detect import VideoHandDetector

for video in os.listdir(RAW_DIR):
    print("processing video ",video)
    video_name = video.split(".")[0]
    hand_detect_process = VideoHandDetector(video_name = video_name, video_path=RAW_DIR+video, output_path=OUTPUT_DIR)
    hand_detect_process.run()
