import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\ADMIN\AppData\Local\Tesseract-OCR\tesseract.exe'
from PIL import Image
import pyttsx3
import cv2
import gtts as gt
import os


#project
def speech(text):
    engine = pyttsx3.init()

    engine.setProperty("rate",125)
    voices = engine.getProperty('voices')
    engine.setProperty("voice",voices[1].id)
    engine.say(text)
    engine.runAndWait()


cam = cv2.VideoCapture(0)
img_counter = 1;

'''
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
        img_name = "sample{img_counter}.png".format(img_counter)
        cv2.imwrite(img_name,frame)
        
        print("screenshot taken")
'''





imageUrl = 'sample'+(str)(img_counter)+'.png'
img = Image.open('japan.png')
text1 = tess.image_to_string(img,lang='jpn')
print(text1)   
speech(text1)



'''
To save audio file 

tts = gt.gTTS(text=text1,lang="ta")
tts.save("TamilAud.mp3")
os.system("TamilAud.mp3")
'''




'''
eng = 0
japan = 1
tamil = 2
hindi = 3
'''