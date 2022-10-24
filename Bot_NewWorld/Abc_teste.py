from ctypes.wintypes import tagRECT
import pyautogui

a = 0
b = 0
c = 0

pyautogui.PAUSE = 1

pyautogui.press ("win")
pyautogui.write("teste_mt_foda.txt", interval= 0.1)
pyautogui.press("backspace")
pyautogui.press("enter")
pyautogui.write("Esse foi um teste para automacao de uma tarefa", interval= 0.1)