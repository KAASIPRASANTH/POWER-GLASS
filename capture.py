from email.mime import image
from tkinter.tix import Tree
import cv2
cam = cv2.VideoCapture(0)
cv2.namedWindow("show the written paper")

img_counter = 0;
while True:
    ret,frame = cam.read()

    if not ret:
        print("failed")
        break
    cv2.imshow("test",frame)

    k = cv2.waitKey(1)
    #Esc key
    if k%256 == 27:
        print("Escape hit, closing the app")
        break
    #space key
    elif k%256 == 32:
        img_name = "sample_1{}.png".format(img_counter)
        cv2.imwrite(img_name,frame)
        print("screen shot taken")

cam.release()
cam.destroyAllWindows()