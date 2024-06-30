import pyautogui
import pyperclip #permite digitar com carecteres epeciais, porém te que usar funçao


def escrever_frase(frase): #function
    pyperclip.copy(frase) #copia a frase da função
    pyautogui.hotkey('ctrl','v') #colar
#mover o mouse ate o camp de digitar
pyautogui.moveTo(981,85,duration=2)
#clicar no campo de digitar
pyautogui.click()

#digitar testo
escrever_frase('Automação é incrível') 
