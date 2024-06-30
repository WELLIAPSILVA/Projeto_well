#acesar site do https://pt.wikipedia.org/wiki/Brasil e fazer clicar em um lik especifico

import pyautogui
from time import sleep

pyautogui.moveTo(1469,472,duration=2)
pyautogui.scroll(-2600)
pyautogui.click()