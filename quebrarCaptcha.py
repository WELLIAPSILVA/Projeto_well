#recoonhecimento de imagem simples
import pyautogui

#este laocaliza a imgem que  foi printada e colcaoda na pasta #usa o print pra imprimir os dados na tela
print(pyautogui.locateOnScreen('cap.png'))

#encontrar a coordenada o centro da imagem
print(pyautogui.locateCenterOnScreen('cap.png'))

#clicando no centro do captcha do site da fazenda.gov
pyautogui.click(x=1588, y=568,duration=2)

'''É possível usar o localização encaontra pra clicar em vez e ter que adr print para ver
basta transformar o locatelcenteronscren em variavel e depois puxar as variaveis

exemplo:
captcha= pyautogui.locateCenterOnScreen('cap.png')
pyautogui.click(captcha[0],captcha[1],duration=2)

#no caso acima clicaria automaticamente com o valor que o python encontrou, sempreciar que o usuario
digite os valores no pyautogui.click conforme no incio do código
'''