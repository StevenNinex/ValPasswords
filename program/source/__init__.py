import os
import random
import string
import sys
from time import sleep

from colorama import Fore as F
from pystyle import Colorate, Colors

BANNER: str = """
 _   _       _______                                   _     
| | | |     | | ___ \                                 | |    
| | | | __ _| | |_/ /_ _ ___ _____      _____  _ __ __| |___ 
| | | |/ _` | |  __/ _` / __/ __\ \ /\ / / _ \| '__/ _` / __|
\ \_/ / (_| | | | | (_| \__ \__ \\ V  V / (_) | | | (_| \__ 
 \___/ \__,_|_\_|  \__,_|___/___/ \_/\_/ \___/|_|  \__,_|___/
                                                            
"""

OPTIONS: str = """
[01] Generar Contraseña               [02] Salir del Programa
"""

def Print(text: str):
    print(f"{F.GREEN}[{F.BLUE}+{F.GREEN}] OK: {F.WHITE}{text}")
def Error(text: str):
    print(f"{F.RED}[{F.MAGENTA}-{F.RED}] ERROR: {F.WHITE}{text}")
def Input(text: str):
    print(f"{F.YELLOW}[{F.CYAN}?{F.YELLOW}] INPUT: {F.WHITE}{text}")

clear = lambda: os.system("cls" if os.name=="nt" else "clear")

class ValPasswords:
    def __init__(self):
        self.Start()
    def Start(self):
        self.Banner()
        print(Colorate.Horizontal(Colors.blue_to_green, OPTIONS, 1))
        print("\n")
        Input("Por favor, ingrese una de las opciones anteriormente mostradas:\n")
        option = input(f"{F.YELLOW}Val{F.CYAN}@{F.YELLOW}Root >>{F.WHITE} ")
        self.HandleOptions(option)
    def Banner(self):
        clear()
        print(Colorate.Horizontal(Colors.blue_to_green, BANNER, 1))
    def HandleOptions(self, option):
        if (option=="1") or (option=="01"):
            try:
                self.Generate()
            except Exception as e:
                Error(e)
                sys.exit()
        elif (option=="2") or (option=="02"):
            try:
                self.Exit()
            except Exception as e:
                Error(e)
                sys.exit()
        else:
            Error("Opción inválida")
            sleep(1.5)
            self.Start()
    def Exit(self):
        clear()
        Print("Saliendo... Muchas gracias por utilizar este programa!")
        sys.exit()
    def Generate(self):
        clear()
        self.Banner()
        numbers = 0
        symbols = 0
        x = 0
        print("\n")
        Input("¿Cuál es la longitud deseada para la contraseña? [5 - 16]\n")
        try:
            x = int(input(f"{F.YELLOW}Val{F.CYAN}@{F.YELLOW}Gen >>{F.WHITE} "))
        
            if (x < 5):
                print("\n")
                Error("La longitud no puede ser menor que 5\n")
                sleep(1.5)
                self.Generate()
            elif (x > 16):
                print("\n")
                Error("La longitud no puede ser mayor que 16\n")
                sleep(1.5)
                self.Generate()
            print("\n")
            Input("¿Desea agregar números a su contraseña? [Y/N]\n")
            numbers = input(f"{F.YELLOW}Val{F.CYAN}@{F.YELLOW}Gen >>{F.WHITE} ")
            print("\n")
            if (numbers=="Y") or (numbers=="y"):
                numbers = 1
            else:
                numbers = 0
            Input("¿Desea agregar símbolos a su contraseña? [Y/N]\n")
            symbols = input(f"{F.YELLOW}Val{F.CYAN}@{F.YELLOW}Gen >>{F.WHITE} ")
            print("\n")
            if (symbols=="Y") or (symbols=="y"):
                symbols = 1
            else:
                symbols = 0
            
            if (numbers==1) and (symbols==0):
                vocabulary = (string.ascii_letters + string.digits)
                password = "".join(random.choice(vocabulary) for _ in range (x))
                self.Banner()
                Print(f"Contraseña generada: {password}\n")
                Input("Pulse ENTER para salir al menú")
                input("")
                self.Start()
            elif (numbers==0) and (symbols==1):
                vocabulary = (string.ascii_letters + string.punctuation)
                password = "".join(random.choice(vocabulary) for _ in range (x))
                self.Banner()
                Print(f"Contraseña generada: {password}\n")
                Input("Pulse ENTER para salir al menú")
                input("")
                self.Start()
            elif (numbers==1) and (symbols==1):
                vocabulary = (string.ascii_letters + string.punctuation + string.digits)
                password = "".join(random.choice(vocabulary) for _ in range (x))
                self.Banner()
                Print(f"Contraseña generada: {password}\n")
                Input("Pulse ENTER para salir al menú")
                input("")
                self.Start()
            elif (numbers==0) and (symbols==0):
                vocabulary = (string.ascii_letters)
                password = "".join(random.choice(vocabulary) for _ in range (x))
                self.Banner()
                Print(f"Contraseña generada: {password}\n")
                Input("Pulse ENTER para salir al menú")
                input("")
                self.Start()
            else:
                Error("Por favor, siga las instrucciones")
                sleep(1.5)
                self.Start()
            
        except ValueError:
            Error("El valor tiene que ser un número")
            sleep(1.5)
            self.Generate()

if (__name__=="__main__"):
    try:
        ValPasswords()
    except Exception as e:
        Error(e)
        sys.exit()