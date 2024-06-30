#como digitar
import pyautogui
#mover o mouse ate o camp de digitar
pyautogui.moveTo(1585,1009,duration=2)
#clicar no campo de digitar
pyautogui.click()

#digitar testeo
pyautogui.typewrite('Olá, bom dia')#obs, este não aceita careteres epeciais

#clicar em enviar
pyautogui.click(1880,1003,duration=2)
