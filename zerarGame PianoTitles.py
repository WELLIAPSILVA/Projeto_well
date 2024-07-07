#zera jogo piano titles com pyatutogui

'''para solcuionar basta achar 4 pontos na tela e ver quando ele mudar de cor clicar
# o While usado abaico é o que gera uma repetiçao para ficar rodando infinitamente.
# o click do pyautogui não funcio na tão rapido para pode usar neste jogo então temos que usar a
bibliotenca win32api e win32con

'''
import pyautogui
import keyboard
import win32api #usada pra cria função de clicar
import win32con #usada pra cria função de clicar
from time import sleep

pyautogui.click(1312,578,duration=1)#para clicar no botao de star do jogo

def click(x,y): #funçao paraclicar
    win32api.SetCursorPos((x,y))#seleciona a posição do mouse
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) # comando para o apertar o mouse
    sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)#comando para solar o mouse



while keyboard.is_pressed('1')== False:
  if  pyautogui.pixelMatchesColor(1324,539,(0,0,0)):
    click(1324,539)
    
  if pyautogui.pixelMatchesColor(1402,541,(0,0,0)):
    click(1402,541)
    
  if pyautogui.pixelMatchesColor(1475,541,(0,0,0)):
    click(1475,541)
    
  if pyautogui.pixelMatchesColor(1557,540,(0,0,0)):
    click(1557,540)
    
    
#link do jogo https://www.jogos360.com.br/piano_tiles_2_online.html