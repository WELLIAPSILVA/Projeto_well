#como digitar
import pyautogui
import pyperclip #permite digitar com carecteres epeciais, porém te que usar funçao


def escrever_frase(frase): #function
    pyperclip.copy(frase) #opia a frase da função
    pyautogui.hotkey('ctrl','v') #copiar
#mover o mouse ate o camp de digitar
pyautogui.moveTo(1585,1009,duration=2)
#clicar no campo de digitar
pyautogui.click()

#digitar testo
escrever_frase('Olá, bom dia') #frase que sera usada na função acima
#pyautogui.typewrite('Olá, bom dia')#obs, este não aceita careteres epeciais

#clicar em enviar
pyautogui.click(1880,1003,duration=2)
