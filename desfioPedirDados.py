import pyautogui as pa 
from time import sleep
import pyperclip as pe

email= pa.prompt(text='digite seu en-mail',title='Email')
Senha= pa.password(text='Digite sua senha',title='Login',mask='*')
pe.copy(email)
pa.click(988,106)
sleep(0.5)
pa.hotkey('ctrl','v')
pa.press('enter')
pe.copy(Senha)
pa.hotkey('ctrl','v')


