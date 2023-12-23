import pyautogui
import time
pyautogui.PAUSE = 3


# ABRIR O NOTION  
pyautogui.hotkey("win" , "r")
pyautogui.press("enter")
pyautogui.write("cd desktop")
pyautogui.press("enter")
pyautogui.write("notion.lnk")
pyautogui.press("enter")
#----------------------------


# ABRIR O INTELLIJ , CHROME , YOUTUBE 
pyautogui.hotkey("win" , "r")
pyautogui.press("enter")
pyautogui.write("start chrome")
pyautogui.press("enter")
pyautogui.hotkey("alt" , "tab")
pyautogui.write("cd desktop")
pyautogui.press("enter")
pyautogui.write("intellij.lnk")
pyautogui.press("enter")
pyautogui.hotkey("win" , "r")
pyautogui.press("enter")
pyautogui.write("cd desktop")
pyautogui.press("enter")
pyautogui.write("youtube.lnk")
pyautogui.press("enter")
#--------------------------------------

# minimixar tudo
time.sleep(20)
pyautogui.hotkey("win" , "m")