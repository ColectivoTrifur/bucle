#!python3
from bucle.scripts import constants
from bucle.processors.hand_detect import VideoHandDetector
from bucle.processors.face_detect import VideoFaceDetector

import click
import os

# en un futuro esto será un worker
@click.command()
def process():
    #TODO: reemplazar por sacar de una cola de redis
    RAW_DIR = constants.RAW_DIR
    OUTPUT_DIR = constants.OUTPUT_DIR
    for video in os.listdir(constants.RAW_DIR):
        click.secho(f"[*] Processing video {video}",fg='blue', bold=True)
        video_name = video.split(".")[0]
        click.echo("[*] Processing hands")
        hand_detect_process = VideoHandDetector(video_name = video_name, video_path=RAW_DIR+video, output_path=OUTPUT_DIR)
        hand_detect_process.run()
        click.echo("[*] Processing faces")
        face_detect_process = VideoFaceDetector(video_name = video_name, video_path=RAW_DIR+video, output_path=OUTPUT_DIR)
        face_detect_process.run()
        click.secho("[*] Finished all processing\nByee!",fg='blue', bold=True)

if __name__ == '__main__':
    process()
    #visualize()
