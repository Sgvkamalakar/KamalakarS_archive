# import webbrowser
# import time
# que=input("Have you connected me in Twitter and LinkedIn? (Y/N): ")
# if que=="Y" or que=='y':
# 	print("Thanks for connecting")
# elif que=="N" or que=='n':
#     print('Please connect........')
#     time.sleep(2)
#     webbrowser.open("https://twitter.com/sgvkamalakar")
#     time.sleep(3)
#     webbrowser.open("https://www.linkedin.com/in/gowri-vinay-kamalakar-satapathi-9a6556213/")
#     time.sleep(3)
#     print('Thanks for connecting')
# import pywhatkit as kit 
# number='9701701113'
# kit.sendwhatmsg(number,'hi',23,18)
import webbrowser                  # for opening whatsapp web using the default browser
import pyautogui as pt           # for automate the movement and clicks of keyboard and mouse.
import time

webbrowser.open('https://web.whatsapp.com/send?phone= +91 970-170-1113-')#,&text=Hey!')
message=input('Enter message:')
# phone = "number with country code to which you want to send the message" -> eg: +91 xxx-xxx-xxxx 
# text = "text that you want to send" -> eg: send = HEY!! (this will show "HEY" on the sender's message box but will not send it)
pt.typewrite(message)
time.sleep(1)                      # In case whatsapp'll take time to open due to internet connectivity.

pt.press("enter")                   # This will automatically press "enter" on the keyboard & message will be send.