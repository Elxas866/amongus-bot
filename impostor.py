from pyautogui import *
from keyboard import *
from time import sleep


# killbutton pixel info
x = 1281
y = 571
red = 219

sleep(2)

while not is_pressed('q'):
    if pixel(x, y)[0] == red:
        click(x, y)