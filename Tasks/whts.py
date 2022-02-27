from argparse import HelpFormatter
import pyautogui 
import webbrowser as web 
import time



i = 0
while i<100:
    time.sleep(0.5)
    pyautogui.typewrite("From Russia !!!")
    time.sleep(0.2)
    pyautogui.press("enter")
    i+=1

