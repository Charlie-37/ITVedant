from argparse import HelpFormatter
import pyautogui 
import webbrowser as web 
import time



i = 0
while i<5:
    time.sleep(0.5)
    pyautogui.typewrite("Sadla Mahatre")
    time.sleep(0.2)
    pyautogui.press("enter")
    i+=1





