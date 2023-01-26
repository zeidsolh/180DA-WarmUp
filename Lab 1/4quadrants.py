import cv2
import random
import time
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

detector = HandDetector(detectionCon=0.8, maxHands=2)

current_time = int(time.time())
random_number1 = random.randint(0, 1)
random_number2 = random.randint(0, 1)


font                   = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (30,450)
fontScale              = 1
fontColor              = (255,255,255)
thickness              = 1
lineType               = 2

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, draw = True)
    if(int(time.time()) -  current_time > 0):
        current_time = int(time.time())
        random_number1 = random.randint(0, 1)
        random_number2 = random.randint(0, 1)
    cv2.rectangle(img, (0+320*random_number1, 0+240*random_number2), (320+320*random_number1, 240+420*random_number2), (255, 0, 0), 2)
    if hands:
        hand1 = hands[0]
        lmList1 = hand1["lmList"]
        palm_position = lmList1[0]
        print(palm_position)
        if(0+320*random_number1 <= palm_position[0] <= 320+320*random_number1
        and 0+240*random_number2 <= palm_position[1] <= 240+420*random_number2):
            cv2.putText(img,'Inside Quadrant', 
                        bottomLeftCornerOfText, 
                        font, 
                        fontScale,
                        fontColor,
                        thickness,
                        lineType)
    cv2.imshow("Image", img)
    cv2.waitKey(1)

