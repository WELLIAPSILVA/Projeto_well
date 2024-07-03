#recoonhecimento de imagem simples
import pyautogui

#este laocaliza a imgem que  foi printada e colcaoda na pasta #usa o print pra imprimir os dados na tela
print(pyautogui.locateOnScreen('cap.png'))

#encontrar a coordenada o centro da imagem
print(pyautogui.locateCenterOnScreen('cap.png'))

#clicando no centro do captcha do site da fazenda.gov
pyautogui.click(x=1588, y=568,duration=2)