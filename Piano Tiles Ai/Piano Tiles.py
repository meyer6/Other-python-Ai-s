import time
from ctypes import windll
  
import keyboard
from pynput.mouse import Button, Controller
def getpixel(x,y):
    return rgba(windll.gdi32.GetPixel(dc,x,y))
def rgba(colorref):
    mask = 0xff
    return [(colorref & (mask << (i * 8))) >> (i * 8) for i in range(4)] 

dc= windll.user32.GetDC(0)
mouse = Controller()   

time.sleep(5)   

while keyboard.is_pressed('q')==False:
    y=580
    for x in range(722,1023,100):
        rgb = getpixel(x,y)
        if rgb[0] > 50 and rgb[0] < 60 and rgb[1] > 155 and rgb[1] < 165 and rgb[2] > 193 and rgb[2] < 203:
            mouse.position = (x/1.5, y/1.5)
            mouse.click(Button.left)
        elif rgb[0]<25:
            mouse.position = (x/1.5, y/1.5)
            mouse.press(Button.left) 

    time.sleep(0.011)
            