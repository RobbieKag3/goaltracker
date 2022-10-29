import cv2
import time
import math
goalx=530
goaly=300
video=cv2.VideoCapture("PRO-C107-Reference-Code-main/bb3.mp4")
tracker=cv2.TrackerCSRT_create()
ret,img=video.read()
bbox=cv2.selectROI("trscking", img,False)
tracker.init(img,bbox)
def drawbox(img,bbox):
    x,y,w,h=int(bbox[0]),int(bbox[1]), int(bbox[2]), int(bbox[3])
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3,1)
def goaltracking(img,bbox):
    x,y,w,h=int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    c1=x+int(w/2)
    c2=y+int(h/2)
    cv2.circle(img,(c1,c2),2,(0,0,255),3)
    dist=math.sqrt((c1-goalx)**2+(c2-goaly)**2)
    if dist<=20:
        cv2.putText(img,"Goal",(300,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)

while True:
    ret,img=video.read()
    success,bbox=tracker.update(img)
    drawbox(img,bbox)
    goaltracking(img,bbox)
    cv2.imshow("result",img)
    if cv2.waitKey(1)==32:
        break