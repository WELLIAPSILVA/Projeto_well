#como usar botões e atalhos do teclado
import pyautogui
from time import sleep
#navegar e clicar no campo e mail
pyautogui.click(1411,265,duration=2)
sleep(1)
#igittar o o e- mail
pyautogui.typewrite('welliapsilva@gmail.com') 
sleep(1)
#apertar tab para o proximo campo
pyautogui.press('tab')
sleep(1)
#digitar senha
pyautogui.typewrite('112345') #caso a senha tenha caracteres especiais usar função
#apertar tab
pyautogui.press('tab')
sleep(1)
#apertar espaço
pyautogui.press('space')

#digite o codigo abaixo para ver todas as teclas que pode digiar
#print(pyautogui.KEYBOARD_KEYS) #Deixei comenta do pra gravar