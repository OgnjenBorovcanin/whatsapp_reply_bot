import pyautogui as pt
from time import sleep

while True:
    posXY = pt.position() #vraca poziciju pointera
    print(posXY, pt.pixel(posXY[0], posXY[1])) #printuje poziciju pointera i boje preko kojih pointer prelazi
    sleep(1)
    if posXY[0] == 0:
        break