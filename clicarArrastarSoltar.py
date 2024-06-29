#como pegar e arrastar algo pra outro lugar
import pyautogui
for i in range(9):#função pra repetir o codigo abaixo 9x
    #mover mouse ate ma coordenada
    pyautogui.moveTo(1423,478,duration=0.5)
    # clicar e arrastar ate um ponto e soltar
    pyautogui.dragTo(1360,790,button='left',duration=0.5)
    #repetir 9x para cada arquivo (ou ajustar as vezez para quantos arquivos tiver)
    #para repetir bastar transforma o codigo em função

#Exemplo de aplicação:
# isso pode ser usa inclusve para mandar imagens para contaso e mum chat