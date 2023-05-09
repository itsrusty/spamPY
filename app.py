import pyautogui as pg, webbrowser as web, time as tm  
from colorama import init, Back, Fore

init()

# ENTER number phone
numberVictim = input(Fore.GREEN + "Ingresa el numero de la persona: ")

# MESSAGE
messageVictimInput = input(Fore.BLUE + "Ingresa el mensaje a enviar: ")

# Times
times = input(Fore.RED + "Ingresa las veces que se enviará el mensaje: ")

# open a web browser
web.open("https://web.whatsapp.com/send?phone=+521" + numberVictim)

for i in range(int(times)):
    pg.write(messageVictimInput)
    pg.press('enter')