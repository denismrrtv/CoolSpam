
import pyautogui
import webbrowser
import time
import os
import re

from colorama import Fore

ruToen = {
	'й':'q',
	'ц':'w',
	'у':'e',
	'к':'r',
	'е':'t',
	'н':'y',
	'г':'u',
	'ш':'i',
	'щ':'o',
	'з':'p',
	'х':'[',
	'ъ':']',
	'ф':'a',
	'ы':'s',
	'в':'d',
	'а':'f',
	'п':'g',
	'р':'h',
	'о':'j',
	'л':'k',
	'д':'l',
	'ж':';',
	'э':"'",
	'я':'z',
	'ч':'x',
	'с':'c',
	'м':'v',
	'и':'b',
	'т':'n',
	'ь':'m',
	'б':',',
	'ю':'.',
	'!':'!',
	'?':'?',
	'@':'@',
	'#':'#',
	'`':'`',
	'~':'~',
	'$':'$',
	'%':'%',
	'^':'^',
	'&':'&',
	'*':'*',
	'(':'(',
	')':')',
	'_':'_',
	'+':'+',
	'=':'=',
	'-':'-',
	'/':'/',
	'1':'1',
	'2':'2',
	'3':'3',
	'4':'4',
	'5':'5',
	'6':'6',
	'7':'7',
	'8':'8',
	'9':'9',
	'0':'0',
	' ' : ' '
}

def clear ():
    if os.name == 'nt': 
        _ = os.system('cls') 
    else: 
        _ = os.system('clear')

def spam (message, repeats, delay):
	for i in range(repeats):         #
		if message != "":
			pyautogui.typewrite(message)     
			pyautogui.press("enter")
		else:
			pyautogui.hotkey('ctrl', 'v')      
			pyautogui.press("enter")

		time.sleep(delay)


	print(Fore.GREEN + "Хорошая работа, Олег!\n")


def main ():

	print ('''
Наш телеграмчик: @Termuxtop
 ▄▄·             ▄▄▌  .▄▄ ·  ▄▄▄· ▄▄▄· • ▌ ▄ ·. 
▐█ ▌▪▪     ▪     ██•  ▐█ ▀. ▐█ ▄█▐█ ▀█ ·██ ▐███▪
██ ▄▄ ▄█▀▄  ▄█▀▄ ██▪  ▄▀▀▀█▄ ██▀·▄█▀▀█ ▐█ ▌▐▌▐█·
▐███▌▐█▌.▐▌▐█▌.▐▌▐█▌▐▌▐█▄▪▐█▐█▪·•▐█ ▪▐▌██ ██▌▐█▌
·▀▀▀  ▀█▄▀▪ ▀█▄▀▪.▀▀▀  ▀▀▀▀ .▀    ▀  ▀ ▀▀  █▪▀▀▀	
		''')

	message = input("Какое сообщение вы хотите отправлять: ").lower ()
	repeats = int(input("Сколько сообщений вы хотите отправить: "))
	delay = int(input("Задержка между сообщениями: "))



	print("Нажмите мышкой на поле ввода, а потом нажмите 'Enter'. Через 5 секунд запустится спам!")

	time.sleep (5)

	if re.findall (r'[^йцукенгшщзхъфывапролджэячсмитьбю]', message) == []:  
		spam (message, repeats, delay)

	else:

		messEN = []
		messENstr = ''

		for i in list(message):
			for key in ruToen:
				if i == key:
					i = ruToen[key]
					messEN.append (i)
					messENstr = ''.join(messEN)


		spam (messENstr, repeats, delay)

if __name__ == '__main__':
	clear ()
	main ()