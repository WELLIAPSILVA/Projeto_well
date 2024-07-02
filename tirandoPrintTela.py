#Como tirar print da tela inteira ou parte dela
import pyautogui


#tirar print de uma tela inteira
pyautogui.screenshot('tela.jpg')

#tirar print d eparte da tela
#pyautogui.screenshot('janela.jpg',region=(1426,159,280,506))#capitura a localização inicial do mouse, e deois coloque quantos pixesl pra direito e para baixo

''' segue mensagem de problema que estou esto tendo ao executar

PS C:\Users\WellingtonAS\Documents\Python Projetos\Projeto_well> & C:/Users/WellingtonAS/AppData/Local/Programs/Python/Python312/python.exe "c:/Users/WellingtonAS/Documents/Python Projetos/Projeto_well/tirandoPrintTela.py"
Traceback (most recent call last):
  File "c:\Users\WellingtonAS\Documents\Python Projetos\Projeto_well\tirandoPrintTela.py", line 6, in <module>
    pyautogui.screenshot('tela.jpg')
  File "C:\Users\WellingtonAS\AppData\Local\Programs\Python\Python312\Lib\site-packages\pyautogui\__init__.py", line 228, in _couldNotImportPyScreeze
    raise PyAutoGUIException(
pyautogui.PyAutoGUIException: PyAutoGUI was unable to import pyscreeze. (This is likely because you're running a version of Python that Pillow (which pyscreeze depends on) doesn't support currently.) Please install this module to enable the function you tried to call.'''