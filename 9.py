import cv2

camera = cv2.VideoCapture(0)
while True:
    success, img = camera.read()
    if success:
        cv2.imshow('video', img)
    
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
    camera.release()
    cv2.destroyAllWindows()