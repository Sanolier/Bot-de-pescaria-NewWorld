import pyautogui
import time
r= None

while r is None:
   try:
    if pyautogui.locateOnScreen ('nam.png'):
        print("ta na tela")
    else:
        print("nao ta na tela")
    break
   except Exception as e:
      r = None
   