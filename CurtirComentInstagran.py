'''
bot de curdidas e comentario instagram

1- navegar ate a o site do instragram
2- entrar com seu usuario
3- entrar com a senha
4- clicar em login
5- clicar em 'not now' para não salvar no navegador
6- fechar janela de "salvar senha"
7- pesquisar pela pagina
8- entar na pagina
9- clicar na primiera postagem mais recente
10- verificar se já curti ou não aquela postagem
11- se ja tiver curtido fazer nada, pasar o bot por 24 horas
12- se não tiver curtido, curtir a foto
13- se não tiver curtido comentar a foto
14- pausar por 24 horas
15- após 24 hora rodar tudo de novo
'''   
import pyautogui as pa 
import webbrowser as wb 
from time import sleep
login= pa.prompt(text='Digite seu login',title='login')#solicita o usuario
senha= pa.password(text='Digite sua senha',title='senha',mask='*')#solicita a senha
pagina= pa.prompt(text='Digite o nome da pagina a buscar',title='Pagina do insta')#solicita a pagina a buscar

wb.open_new('https://www.instagram.com/')
sleep(4)
usu=pa.locateCenterOnScreen('instUser.png')
pa.moveTo(usu[0],usu[1])
pa.move(0,90,duration=0.5)
pa.doubleClick()
sleep(1)
pa.typewrite(login)
pa.move(-90,40,duration=1)
pa.doubleClick()
pa.typewrite(senha)
pa.move(-30,50,duration=1)#clica no botao de login
pa.click(duration=1)
sleep(5)
save=pa.locateCenterOnScreen('agoraNao.png')#clicar em 'not now' para não salvar no navegador
pa.click(save[0],save[1],duration=0.5)
sleep(5)
lupa=pa.locateCenterOnScreen('buscar.png')#clicar em buscar para digitar a pagina
pa.click(lupa[0],lupa[1],duration=0.5)
sleep(3)
pa.typewrite(pagina)#digitando a pagina
sleep(2)
page= pa.locateCenterOnScreen('nike.png')#clicar em 'not now' para não salvar no navegador
pa.click(page[0],page[1],duration=0.5)
sleep(3)
public=page= pa.locateCenterOnScreen('publicacoes.png')#navega a ate a escria publicações proximo a ultima publicação
pa.moveTo(public[0],public[1])
pa.move(0,-40,duration=0.5)
pa.click()
sleep(5)
coracao= pa.locateCenterOnScreen('coracao.png')
coracao2= pa.locateCenterOnScreen('coracao2.png')
if coracao is not None:
    sleep(86400)
elif coracao == None:
    pa.click(coracao2[0],coracao2[1],duration=1)
    sleep(3)
    pa.move(40,0,duration=0.5)
    pa.click()
    pa.typewrite('gostei desta foto')
    pa.press('enter')
    sleep(86400)