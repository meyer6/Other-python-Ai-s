import keyboard
import time
import pyautogui
from PIL import ImageGrab
import sys


def exit():
    if keyboard.is_pressed('q'):
        sys.exit()

def move(num, change):
    for _ in range(num):
        exit()
        pause()
        keyboard.press_and_release(change)
        time.sleep(0.35)
        
def colourRange(num1, num2):
    if num1 > num2 - 20 and num1 < num2 + 20:
        return True
    return False
        
def checkColour(x, y, r1, g1, b1, check):
    exit()
    pause()
    image = ImageGrab.grab((x, y, x+2, y+2), include_layered_windows=False, all_screens=True)
    rgb_im = image.convert('RGB')
    r, g, b = rgb_im.getpixel((1, 1))
    if colourRange(r, r1) and colourRange(g, g1) and colourRange(b, b1):
        if abs(r-b) > 3 or check:
            return True
    return False

def click(coords):
    exit()
    pause()
    pyautogui.moveTo(coords[0], coords[1])
    pyautogui.click()
    time.sleep(0.4)
    
def changePokemon(deadPokemon, fight, poke, move5):
    click(poke)
    while checkColour(*deadPokemon, False) == False:
        if checkColour(*fight, False):
            click(fight)
            click(move5)
        time.sleep(1)
def pause():
    if keyboard.is_pressed('z'):
        while keyboard.is_pressed('x') == False:
            exit()
            time.sleep(2)
            
deadPokemon = [950, 267, 26, 27, 31]
pokemonChange = [688,1031, 31, 98, 141]
poke1 = [960, 300]
poke2 = [960, 380]
poke3 = [960, 450]
poke4 = [960, 530]
fight = [900, 950, 170, 40, 38]
move1 = [830, 850]
move2 = [1080, 850]
move3 = [830, 950]
move4 = [1080, 950]

time.sleep(5)

while True:
    move(5, "d")
    move(2, "s")
    move(3, "d")
    move(10, "w")
    move(12, "d")
    move(5, "w")
    move(1, "a")
    move(2, "w")

    while checkColour(*pokemonChange, True) == False:
        keyboard.press_and_release("space")
        time.sleep(0.5)
        
    click(pokemonChange[:2])
    time.sleep(0.8) 
    
    changePokemon(deadPokemon, fight, poke2, move3)
    changePokemon(deadPokemon, fight, poke3, move2)

    
    click(poke2)
    while checkColour(600, 10, 0, 0, 0, True) == True: 
        if checkColour(*fight, False):
            click(fight)
            click(move1)
        time.sleep(1)

    time.sleep(2)
    for _ in range(5):
        keyboard.press_and_release("space")
    time.sleep(5)


