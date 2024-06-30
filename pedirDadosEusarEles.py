import pyautogui

email = pyautogui.prompt(text='Digite seu e-mail:',title='informações Obrigatórias')
print(f'voce digitou: {email}')