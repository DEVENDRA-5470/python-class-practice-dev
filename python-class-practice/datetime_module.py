# from datetime import datetime
# import time
# time.sleep(5)
# c=datetime.now().strftime("%A %d-%B-%Y, %H:%M:%S")
# print(c)

import pyautogui
import time
time.sleep(5)
for i in range(10):
    pyautogui.typewrite("Hello How are" , interval=0.05)