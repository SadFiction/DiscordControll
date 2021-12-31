from sys import *
import os
import time

from discord.ext import commands




class setup:
    
    
    def run(self):
        self.__install()
        self.__create_data_files()
    def __install(self):
        try:
            import installing_simplejson as in_simple
            in_simple.install()
        except(ModuleNotFoundError):
            print("\n### Could not install simplejson ###\n")

        import installing_pycordAlpha as in_pycord
        if platform == "win32":
            try:
                os.system("py -m pip uninstall discord")
                os.system('cls||clear')
            except(Exception):
                pass
            try:
                in_pycord.install()
            except(Exception):
                print("\n### Could not install Pycord ###\n")
    
    def __create_data_files():
        location = "./"

        if "Code/setup.py" in (argv[0]).replace("\\", "/"):
            location = (argv[0].replace("\\", "/")).replace("Code/setup.py" , "")
        try:
            with open(f"{location}data/token.txt" , "x") as file:
                token = input("\nPlease enter bot token: ")
                file.write(token.strip())
                file.close
        except(Exception):
            print("Something went wrong with the token.txt file")
        try: 
            with open(f"{location}data/guild_id.txt" , "x") as file:
                guild_id = input("\nEnter your guild id: ")
                
                file.write(guild_id.strip())
                file.close()
        except(Exception):
            print("Something went wrong with the guild_id.txt file")
        try:
            with open(f"{location}data/command_channel_id.txt" , "x") as file:
                command_id = input("Please enter the id of the command channel...")
                file.write(command_id.strip())
                file.close()
        except(Exception):
            print("Something went wrong with the command_channel_id.txt file")
        
        try:
            with open(f"{location}data/screenshot_channel_id.txt" , "x") as file:
                screenshot_id = input("lease enter the id for the screenshot channel...")
                file.write(screenshot_id.strip())
                file.close()
        except(Exception):
            print("Something went wrong with the screenshot_channel_id.txt")


if __name__ == "__main__":
    if platform == "win32":
        setup().run()
        input()
    else:
        print(f"\n ### {platform.capitalize()} is not supported. Please close this window.###\n")
        
else:
    print(f"\n ### Can't run file fron another file (name must be \"__main__\", yours was \"{__name__}\" ). ###\n")
    input()
	
