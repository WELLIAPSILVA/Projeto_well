'''
Desafio
1)Navegue até o site https://cursoautomacao.netlify.app/
2) Encontre e clique no campo "Digite seu nome" dentro de "exemplos Alertas" e digite seu nome
3) Clique em alerta, para gerar a alerta
4) Feche a alerta
5) Suba a página totalmente para cima
6) Desça apenas o suficiente para conseguir chegar até a secção que contém os arquivos para o quais irá fazer o download e click no botão de download para realizar o downlaod dos arquivos excel e pdf.
7) Depois de ter feito isso, crie uma alerta que diz "VOCÊ TERMINOU"
'''
import webbrowser
import pyautogui
from time import sleep

webbrowser.open_new('https://cursoautomacao.netlify.app/')
sleep(1)
pyautogui.moveTo(2140,256,duration=1)
sleep(0.5)
pyautogui.scroll(-1000)
pyautogui.click(2529,376,duration=0.5)
sleep(1)
pyautogui.typewrite('wellington Aparecido Silva')
sleep(0.5)
pyautogui.click(2527,409,duration=1)
sleep(0.5)
pyautogui.click(2474,191,duration=1)
sleep(1)
pyautogui.scroll(1100)
sleep(1)
pyautogui.scroll(-2000)
pyautogui.click(2040,829,duration=0.5)
sleep(2)
pyautogui.click(2514,504,duration=0.5)
sleep(2)
pyautogui.click(2271,818,duration=0.5)
sleep(2)
pyautogui.click(2518,511,duration=0.5)
sleep(2)
pyautogui.alert('VOCÊ TERMINOU')