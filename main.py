import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\ADMIN\AppData\Local\Tesseract-OCR\tesseract.exe'
from PIL import Image
import pyttsx3
import cv2

def speech(text):
    engine = pyttsx3.init()
    engine.setProperty("rate",125)
    voices = engine.getProperty('voices')
    engine.setProperty("voice",voices[0].id)
    engine.say(text)
    engine.runAndWait()


cam = cv2.VideoCapture(0)
img_counter = 2;
while True:
    ret,frame = cam.read()

    if not ret:
        print("failed")
        break
    cv2.imshow("test",frame)

    k = cv2.waitKey(1)
    #Esc key -> to exit from the photo
    if k%256 == 27:
        print("Escape hit, closing the app")
        break
    #space key -> To take the photo click on to the space button
    elif k%256 == 32:
        img_name = "sample_{}.png".format(img_counter)
        cv2.imwrite(img_name,frame)
        print("screenshot taken")


img = Image.open('sample.png')
text = tess.image_to_string(img)
print(text)   
speech(text)