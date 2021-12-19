#!python3
from bucle.scripts import constants
from bucle.processors.hand_detect import VideoHandDetector
from bucle.processors.face_detect import VideoFaceDetector
from bucle.processors.face_mesh import VideoFaceMesh

import click
from glob import glob
import os
from tqdm import tqdm

def generate_videos():
    OUTPUT_DIR = constants.OUTPUT_DIR
    frames_dirs = glob("./current_outputs/*/")
    for directory in tqdm(frames_dirs):
        print(directory)
        name = directory.split("outputs")[1]
        name = name.replace("/","_")
        command= "cat " + directory +"*.png | ffmpeg -framerate 30 -f image2pipe -i - ./output"+name+".mp4"
        print(command)
        os.system(command)


# en un futuro esto será un worker
@click.command()
def process():
    #TODO: reemplazar por sacar de una cola de redis
    RAW_DIR = constants.RAW_DIR
    OUTPUT_DIR = constants.OUTPUT_DIR
    for video in os.listdir(constants.RAW_DIR):
        click.secho(f"[*] Processing video {video}",fg='yellow', bold=True)
        video_name = video.split(".")[0]
        #click.echo("[*] Processing hands")
        #hand_detect_process = VideoHandDetector(video_name = video_name, video_path=RAW_DIR+video, output_path=OUTPUT_DIR)
        #hand_detect_process.run()
        #click.echo("[*] Processing faces")
        #face_detect_process = VideoFaceDetector(video_name = video_name, video_path=RAW_DIR+video, output_path=OUTPUT_DIR)
        #face_detect_process.run()
        #face_mesh_process = VideoFaceMesh(video_name = video_name, video_path=RAW_DIR+video, output_path=OUTPUT_DIR)
        #face_mesh_process.run()
    click.secho("[*] Finished all processing\n\n",fg='green', bold=True)
    click.secho("[*] Generating output videos",fg='yellow', bold=True)
    generate_videos()
    click.secho("[*] Finished all videos\n\n",fg='green', bold=True)

if __name__ == '__main__':
    process()
    #visualize()
