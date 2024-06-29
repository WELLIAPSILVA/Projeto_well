#como usar a funçao click
import pyautogui
#click personalizado
pyautogui.click(x=1000,y=500,clicks=2,interval=0.0,button='left',duration=2)
#click posição atual (com botão esquerdo)
pyautogui.click()#clica onde esta o mouse parado
pyautogui.click(button='left') #clica onde esta o mouse parado com botao esquerdo
pyautogui.click(button='right')#clica onde esta o mouse parado com botao direito
pyautogui.click(button='midle')#clica onde esta o mouse parado com botao do meio

#clicar X vezes
pyautogui.click(clicks=10) #clcia 10x
# funções para cliques
pyautogui.doubleClick()#clica onde esta o mouse parado duas vezes
pyautogui.rightClick() #clica onde esta o mouse parado com botao esquerdo
pyautogui.middleClick()#clica onde esta o mouse parado com botao direito
pyautogui.tripleClick()#clica onde esta o mouse parado tres vezes

