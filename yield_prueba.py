import cv2
def agarrarVideo(video):
    cap = cv2.VideoCapture(video)
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            yield frame 
frames = agarrarVideo("11.mp4")
for frame in frames:
    cv2.imshow("Juego", frame)
    cv2.waitKey(2)
    
