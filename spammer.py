import pyautogui
import webbrowser
import time
import os

from colorama import Fore

def clear ():
    if os.name == 'nt': 
        _ = os.system('cls') 
    else: 
        _ = os.system('clear')

def main ():

	print ('''
Наш телеграмчик: @Termuxtop
 ▄▄·             ▄▄▌  .▄▄ ·  ▄▄▄· ▄▄▄· • ▌ ▄ ·. 
▐█ ▌▪▪     ▪     ██•  ▐█ ▀. ▐█ ▄█▐█ ▀█ ·██ ▐███▪
██ ▄▄ ▄█▀▄  ▄█▀▄ ██▪  ▄▀▀▀█▄ ██▀·▄█▀▀█ ▐█ ▌▐▌▐█·
▐███▌▐█▌.▐▌▐█▌.▐▌▐█▌▐▌▐█▄▪▐█▐█▪·•▐█ ▪▐▌██ ██▌▐█▌
·▀▀▀  ▀█▄▀▪ ▀█▄▀▪.▀▀▀  ▀▀▀▀ .▀    ▀  ▀ ▀▀  █▪▀▀▀
		''')

	message = input("Какое сообщение вы хотите отправлять: ")
	repeats = int(input("Как долго (в секундах) вы хотите его отправлять: "))
	delay = int(input("Задержка между сообщениями: "))


	print("Нажмите мышкой на поле ввода, а потом нажмите 'Enter'")


	for i in range(0,repeats):         #
			if message != "":
				pyautogui.typewrite(message)     
				pyautogui.press("enter")
			else:
				pyautogui.hotkey('ctrl', 'v')      
				pyautogui.press("enter")

			time.sleep(delay/1000)


	print(Fore.GREEN + "Хорошая работа, Олег!\n")


if __name__ == '__main__':
	clear ()
	main ()