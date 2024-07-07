'''
Bot de envio de mensagens via whatsapp
1- lista de contatos
2- enviar individualmente uma mensagem para cada pessoa
3- pausar entre cada envio
#passos para enviar
1-escolher um contato
2-enviar uma mensagem para este contato:
    https://api.whatsapp.com/send?phone=(colocar numero que ira enviar)
3- repetir para outros contatos
'''
import webbrowser
import pyautogui
from time import sleep

telefones = [5545991178776]

for telefone in telefones:
    webbrowser.open(f'https://api.whatsapp.com/send?phone={telefone}')
    sleep(10)
    pyautogui.click(2382,249,duration=1)
    sleep(10)
    escrever= pyautogui.locateCenterOnScreen('mensagenWahts.png')
    pyautogui.cli(escrever[0],escrever[1])
    sleep(2)
    pyautogui.typewrite('Gostaria de fazer uma visita ao zoologico amanha?')
    sleep(5)
    pyautogui.press('enter')
    sleep(300)