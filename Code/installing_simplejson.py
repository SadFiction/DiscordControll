import os
from sys import *
import time

def install():

        
        if platform == "win32":

                os.system("py -m pip install simplejson")
                os.system('cls||clear')
                print("---successful---- simplejson has installed")
                time.sleep(5)
        
        else:
                return ModuleNotFoundError


if __name__ == "__main__":
        install()
