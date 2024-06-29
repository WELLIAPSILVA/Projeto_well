#como pegar e arrastar algo pra outro lugar
import pyautogui
for i in range(6):#função pra repetir o codigo abaixo 6x
    #mover mouse ate ma coordenada
    pyautogui.moveTo(1288,197,duration=0.5)
    # clicar e arrastar ate um ponto e soltar
    pyautogui.dragTo(1323,691,button='left',duration=0.5)
    #repetir 6x para cada arquivo (ou ajustar as vezez para quantos arquivos tiver)
    #para repetir bastar transforma o codigo em função

#Exemplo de aplicação:
# isso pode ser usa inclusve para mandar imagens para contaso e mum chat