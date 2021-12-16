import cv2
from cvzone.HandTrackingModule import HandDetector
import random

#from pythonosc import udp_client

cap = cv2.VideoCapture('./rob.mp4')

cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon=0.8)

magenta = (255, 0, 255)
colorR = magenta
cx, cy = 100, 100
width, height = 100, 100
offset = 0

ip="127.0.0.1" #"The ip of the OSC server")
port=9001
channel="/objects/Icosphere/modifiers/Wireframe/thickness"
#client = udp_client.SimpleUDPClient(ip, port)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    try:
        img = detector.findHands(img)
    except:
        break
    lmList, _ = detector.findPosition(img)
    if lmList:

        # l,_,_ = detector.findDistance(8,12,img)
        l, _, _ = detector.findDistance(4, 8, img)
        print(l)
        with open('distance.csv','a') as file:
            file.write(str(l)+"\n")
        cursor = lmList[8]
        print(cursor)
        with open('cursor.csv','a') as file:
            file.write(str(cursor[0])+','+str(cursor[1])+"\n")
        if (
            l < 40
            and cx - width // 2 < cursor[0] < cx + width // 2
            and cy - height // 2 < cursor[1] < cy + height // 2
        ):
            colorR = (
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255),
            )
            offset += 100
            cx, cy = cursor  # drag
            number_sent = float(l/20)
            #client.send_message(channel, number_sent)
            print(f'OSC MSG sent {number_sent} to {ip}:{port}/{channel}')
        else:
            colorR = magenta
            offset = 0
    cv2.imshow("Image", img)
    cv2.waitKey(1)

