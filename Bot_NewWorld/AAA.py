import pyautogui
import time

from pyscreeze import locateOnScreen

fish = True

time.sleep(5)
pyautogui.press("f3")
print("Apertei F3")
time.sleep(3)
pyautogui.click()
print("Clicado")
time.sleep(2)
while True:
    print(pyautogui.locateOnScreen("clique.png"))
# while fish:
#     time.sleep(0.5)
    
#     if x != None: 
#         fish = False
#         pyautogui.click()
#         print("Clicado")
