#enviar mensagem automaticamente pelo whatsapp
import webbrowser
import pyautogui
from time import sleep
pyautogui.alert(text='Antes de continuar, por favor abra o Whatsapp no windows!',title='ATENÇÃO')

pyautogui.alert(text='Os números a seguir devem ser digitados como o exemplo 5545numero, sendo cod pais, cod ddd, número',title='Alerata sobre o formato')

fone= pyautogui.prompt(text='Digite os fones separados por virgula:',title='Telefones') #pede pro usuario digitar a lista 
mensagem= pyautogui.prompt(text='Digite a mensagema ser enviada:',title='Mesagem') #pede para digitar mensagem
telefones= [x.strip() for x in fone.split(',')]#transforma os numeros digitados em uma lista legivel ao pyton

for telefone in telefones:        #gera a lista derepetição para envio com interalo de 300 segundos
    webbrowser.open(f'https://api.whatsapp.com/send?phone={telefone}')# abre o navegador
    sleep(5)
    abrirwats= pyautogui.locateCenterOnScreen('abrir.png') #localiza o botal de bair no whats app
    sleep(0.2)
    pyautogui.click(abrirwats[0],abrirwats[1],duration=0.1) #clica em abrir o whats
    sleep(3)
    
    pyautogui.typewrite(mensagem) #escreve a mensagem
    sleep(1)
    pyautogui.press('enter') #envia mensagem
    pyautogui.alert(text='Envio Bem Sucedido')
    sleep(300) #aguarda este tempo antes de enviar pro poximo contato
    