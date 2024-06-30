import pyautogui
from time import sleep

pyautogui.moveTo(1470,571,duration=2)

for i in range(500): #isso reaperira o scroll abaixo 500x
    pyautogui.scroll(-1500)
    sleep(2) #coloca dentro do parenteses a quantida de pixes a mexer negativo para baixo e positivo para cima
    #para rodar várias vezes basta adiconar a funão antes do scroll