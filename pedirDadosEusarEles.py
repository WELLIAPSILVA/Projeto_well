import pyautogui
#gera um alerta ao usuario
pyautogui.alert(text='Iniciando aua automação',title='Automaçao de login',button='ok')

#pedir informação ao usuario
email = pyautogui.prompt(text='Digite seu e-mail:',title='informações Obrigatórias')
print(f'voce digitou: {email}')

#confirmar  se algo deve acontecer
resposta= pyautogui.confirm(text='continuar rodando a nossa automação?', title='confirmação', buttons=['sim','não','cancelar'])
if resposta == 'sim':
        print('continuar automação')
elif resposta == 'não':
        print('Encerrando automação')
else:
        print('Operação cancelada')

#solicitar senha
pyautogui.password(text='Digita sua senha',title='dados de login', mask='*')