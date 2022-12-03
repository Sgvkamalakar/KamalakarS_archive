import webbrowser
import time
que=input("Have you connected me in Twitter and LinkedIn? (Y/N): ")
if que=="Y" or que=='y':
	print("Thanks for connecting")
elif que=="N" or que=='n':
    print('Please connect........')
    time.sleep(2)
    webbrowser.open("https://twitter.com/sgvkamalakar")
    time.sleep(3)
    webbrowser.open("https://www.linkedin.com/in/gowri-vinay-kamalakar-satapathi-9a6556213/")
    time.sleep(3)
    print('Thanks for connecting')
