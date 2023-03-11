import time
from pynput.keyboard import Key, Controller
import keyboard as k
from PIL import ImageGrab
import os
import pytesseract
import keyboard
time. sleep(10)

os.remove("sc.png")
image = ImageGrab.grab(bbox=(264,445,1660,500))
image.save('sc.png')

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
sentence=pytesseract.image_to_string(r'C:\Users\meyer\Desktop\Coding\Python\Type\sc.png').lower()

keyboard2 = Controller()
for i in range(9):
    print(sentence)
    for letter in sentence:
        keyboard2.press(letter)
        keyboard2.release(letter)
    keyboard2.press(" ")
    keyboard2.release(" ")
    
    time. sleep(0.4)
    
    os.remove("sc.png")
    image = ImageGrab.grab(bbox=(264,500,1660,550))
    image.save('sc.png')
    
    time. sleep(0.4)
    
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    sentence=pytesseract.image_to_string(r'C:\Users\meyer\Desktop\Coding\Python\Type\sc.png').lower()
