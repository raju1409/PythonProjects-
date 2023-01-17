import random
import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import time

# Press 's' to Start Game 


cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

detector = HandDetector(maxHands=1)
timer = 0
startGame = False
stateResult = False
initialTime = 0
playerMove = 0
Scores = [0, 0]  # [AI, Player]


while True:
    success, img = cap.read()
    imgBG = cv2.imread('Resources/BG.png')

    imgScaled = cv2.resize(img, (0,0), None, 0.875, 0.875)
    imgScaled = imgScaled[:, 80:480]

    # Find Hand
    hand, img = detector.findHands(imgScaled)

    if startGame:
        if stateResult is False:
            timer = time.time() - initialTime
            cv2.putText(imgBG, str(int(timer)), (605, 435), cv2.FONT_HERSHEY_PLAIN, 6, (255, 0, 255), 4)

            if timer>3:
                stateResult = True
                timer = 0

                if hand:
                    hand = hand[0]
                    fingers = detector.fingersUp(hand)
                    if fingers == [0, 0, 0, 0, 0]:
                        playerMove = 1
                    elif fingers == [1, 1, 1, 1, 1]:
                        playerMove = 2
                    elif fingers == [0, 1, 1, 0, 0]:
                        playerMove = 3

                    randomNumber = random.randint(1, 3)

                    imgAI = cv2.imread(f'Resources/{randomNumber}.png', cv2.IMREAD_UNCHANGED)
                    imgBG = cvzone.overlayPNG(imgBG, imgAI, (149, 310))

                    # win Check

                    if (playerMove == 1 and randomNumber == 3) or \
                        (playerMove == 3 and randomNumber == 2) or \
                        (playerMove == 2 and randomNumber == 1):
                        Scores[1] += 1
                    else:
                        Scores[0] += 1

                    print("player Move is : ",playerMove)
                    print(fingers)



    imgBG[234:654, 795:1195] = imgScaled
    if stateResult:
        imgBG = cvzone.overlayPNG(imgBG, imgAI, (149, 310))

    cv2.putText(imgBG, str(Scores[0]), (410, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)
    cv2.putText(imgBG, str(Scores[1]), (1112, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)

    cv2.imshow('BG', imgBG)
    # cv2.imshow('image', img)
    # cv2.imshow('Scaled', imgScaled)
    key = cv2.waitKey(1)

    if key == ord('s'):
        initialTime = time.time()
        startGame = True
        stateResult = False


