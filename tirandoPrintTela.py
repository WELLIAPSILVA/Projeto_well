#Como tirar print da tela inteira ou parte dela
import pyautogui

#tirar print de uma tela inteira
#pyautogui.screenshot('tela.jpg')

#tirar print d eparte da tela
pyautogui.screenshot('janela.jpg',region=(1426,159,280,506))#capitura a localização inicial do mouse, e deois coloque quantos pixesl pra direito e para baixo
