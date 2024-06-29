import pyautogui
from time import sleep

pyautogui.click(1531,516)
sleep(5)
pyautogui.click(1518,423)
sleep(5)
pyautogui.moveTo(1448,394,duration=2)
for i in range(100):
    sleep(0.5)
    pyautogui.click()