import time
from PIL import ImageGrab
import pyautogui
import keyboard
time. sleep(5)

image = ImageGrab.grab(bbox=(0,0,1330,900))
rgb_im = image.convert('RGB')

while keyboard.is_pressed('q')==False:
    for a in range(550,1330,50):
        for c in range(420,900,12):
            if a <1200 or c-150>355:
                r, g, b = rgb_im.getpixel((a, c))
                if r==5 and g==194 and b==14 and keyboard.is_pressed('q')==False:
                    pyautogui.moveTo(a, c-150)
                    pyautogui.mouseDown();
                    time.sleep(0.01)
                    pyautogui.mouseUp();
    image = ImageGrab.grab(bbox=(0,0,1330,900))
    rgb_im = image.convert('RGB')
print("WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW")
