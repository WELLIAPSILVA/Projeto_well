#recoonhecimento de imagem simples
import pyautogui
cnpj= pyautogui.prompt(text='digite o cnpj ',title='CNPJ')

#encontrar a coordenada o centro da imagem
captcha= pyautogui.locateCenterOnScreen('cap.png')
pyautogui.click(1192,597,duration=2)
#digitando o site
pyautogui.typewrite(cnpj)
#clicando no centro do captcha do site da fazenda.gov
pyautogui.click(x=1588, y=568,duration=2)