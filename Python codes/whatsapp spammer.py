import pyautogui as pt
import time
from datetime import datetime
import random
limit = int(input("Enter limit:"))
message=input('Enter message:')
i = 0
time.sleep(5)
while i < (limit):
    pt.typewrite(message)  
    # time.sleep(1)
    pt.press("enter")
    i+=1
 
