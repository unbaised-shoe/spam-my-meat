import pyautogui
import time

time.sleep(5)

spam = open("meat")

while True:
    for word in spam:
        pyautogui.typewrite(word)
        pyautogui.press("enter")
# 
#
#
#


