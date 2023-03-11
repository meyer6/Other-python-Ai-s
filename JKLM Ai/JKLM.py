import time
from tkinter import WORD
from PIL import ImageGrab
import keyboard
import os
import numpy as np
import pyautogui
import pyperclip
    

f=open(r"C:\Users\meyer\Desktop\Coding\Python\JKLM\words.txt","r")
lines=f.read().splitlines()

time. sleep(4)
past=[]

while keyboard.is_pressed('q')==False:
    #time. sleep(0.25)
    image = ImageGrab.grab(bbox=(646,952,648,954))
    rgb_im = image.convert('RGB')
    r, g, b = rgb_im.getpixel((1, 1))
    if r>18 and r<30 and g>17 and g<27 and b>14 and b<24:
        pyautogui.moveTo(735, 558)
        for i in range(2):
            pyautogui.mouseDown();
            pyautogui.mouseUp();
        pyautogui.hotkey('ctrl', 'c')
        s1=pyperclip.paste().upper()
        pyautogui.moveTo(646, 952)
        pyautogui.mouseDown();
        pyautogui.mouseUp();
        print(s1)
        for word in lines:
            if s1 in word and word not in past:
                pyautogui.typewrite(word)
                print(word)
                pyautogui.press('enter')
                past.append(word)
                break;
print("WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW")

##        os.remove("sc.png")
##        image = ImageGrab.grab(bbox=(700,540,767,580))
##        image.save('sc.png')
##
##
##        img = cv2.imread('sc.png')
##        img[img != 255] = 0 
##        cv2.imwrite('sc.png', img)
##
##
##        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
##        s1=str(pytesseract.image_to_string(r'C:\Users\meyer\Desktop\Coding\Python\JKLM\sc.png').upper())
##        s1=s1.replace(" ","")
##        s1 = s1.rstrip("\n")
##        s1=s1.replace("IC)","G")
##        print(s1)
##        
##        if s1=="NIC)":
##            s1="ING"
