import pyautogui as pa 

email= pa.prompt(text='digite seu en-mail',title='Email')
Senha= pa.password(text='Digite sua senha',title='Login',mask='*')
pa.click(988,106,duration=2)
pa.typewrite(email)
pa.press('enter')
pa.typewrite(Senha)
