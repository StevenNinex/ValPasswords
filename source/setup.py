import os
import sys

class Setup:
    def __init__(self):
        if (os.name == "nt"):
            self.Windows()
        else:
            self.Linux()
    def Windows(self):
        try:
            os.system("py -m pip install -r src/console/requirements.txt")
            os.system("cls")
            print("Programa instalado correctamente")
        except Exception as e:
            print(f"Un error ha ocurrido\n{e}")
    def Linux(self):
        try:
            os.system("pip install -r src/console/requirements.txt")
            os.system("clear")
            print("Programa instalado correctamente")
        except Exception as e:
            print(f"Un error ha ocurrido\n{e}")

if (__name__ == "__main__"):
    try:
        Setup()
    except Exception as e:
        print(f"Un error ha ocurrido\n{e}")