import cv2

vid = cv2.VideoCapture("AnthonyShkraba.mp4")

if(vid.isOpened() == False):
    print("Unable to access camera")

#Frame Width
width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))    
print(width)
#Frame Height
height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))    
print(height)
#FPS
fps= int(vid.get(cv2.CAP_PROP_FPS))    
print(fps)


while(True):
    ret,frame = vid.read()

    cv2.imshow("Web cam", frame)

    if cv2.waitKey(30) == 32:
        break

vid.release()