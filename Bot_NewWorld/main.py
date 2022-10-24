import pyautogui
import time

r = None

pyautogui.PAUSE = 1
time.sleep(2)
pyautogui.press("f3")
time.sleep(3)
pyautogui.click()
time.sleep(2)

while r is None:
   try:
      pyautogui.click("Espera.png")
      break
   except Exception as e:
      r = None
   