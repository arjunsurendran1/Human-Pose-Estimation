#import libraries
import cv2
import mediapipe as mp
import time

#creating objects
mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()

#take images
#cap = cv2.VideoCapture('pose estimation/poseVideos/1.mp4')
cap = cv2.VideoCapture(0)

#initialize pTime for calculating fps
pTime=0
while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results  = pose.process(imgRGB)
    #print(results.pose_landmarks)
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks,mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape
            print(id, lm)
            cx,cy = int(lm.x*w), int(lm.y*h)
            cv2.circle(img,(cx,cy),5,(255,0,0),cv2.FILLED)


    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime=cTime
    cv2.putText(img,str(int(fps)),(70,50),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
#    cv2.resize(img,(12,72),fx=0,fy=0, interpolation = cv2.INTER_CUBIC)
    cv2.resize(img,(780, 540),fx=0,fy=0, interpolation = cv2.INTER_AREA)


    cv2.imshow('image', img)

    cv2.waitKey(1)