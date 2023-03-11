from pynput.keyboard import Key, Controller
import keyboard as k
import time
import PIL.ImageGrab
keyboard = Controller()
time.sleep(10)
rgb=PIL.ImageGrab.grab().load()[1909,1053]
while (193, 193, 193)!=rgb and k.is_pressed('q')==False:
    keyboard.press(Key.print_screen)
    keyboard.release(Key.print_screen)
    time.sleep(1)
    keyboard.press(Key.right)
    keyboard.release(Key.right)
    time.sleep(1)
    rgb = PIL.ImageGrab.grab().load()[1909,1053]
