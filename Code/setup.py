from sys import *
import os, time
from xml.dom import WrongDocumentErr

"""Setup Class for windows"""

class setup_win32:

    """Started function (can be accessed by outside scripts)"""
    def run(self):
        self.__install()
        self.__create_data_files()
        self.__createTask()

    """Hidden function that installs the required modules (cannot be accessed by outside scripts)"""
    def __install(self):

        """Installs simplejson (not required but faster in terms of speed that the included json module)"""
        try:
            #imports the installing_simple.py file and executes the install function present in the script
            import installing_simplejson as simple
            simple.install()
        #In case the module could not install (modulenotfounderror returns) the following message will be displayed...
        except(ModuleNotFoundError):
            print("\n### Could not install simplejson ###\n")

        """Installs pynput (required for media control)"""
        try:
            #imports the installing_pynput.py file and executes  the install function present in the script
            import installing_pynput as pyn
            pyn.install()
        #in case the module could not install (modulenotfounderror returns) the following message will be displayed...
        except(ModuleNotFoundError):
            print("\n### Could not install Pynput ###\n")
        
        """Installs pycord and uninstalls the normal discord module if present"""
        #imports the installing_pycord.py file 
        import installing_pycord as in_pycord
        try:
            #uninstalls discord if present 
            os.system("py -m pip uninstall discord")
        except(Exception):
            pass
        #executes the install function in the module above
        try:
            in_pycord.install()
        #in case the module could not install (modulenotfounderror returns) the following message will be displayed...
        except(ModuleNotFoundError):
            print("\n### Could not install Pycord ###\n")
    
    def __create_data_files(self):
        location = "./"
        if "Code/setup.py" in (argv[0]).replace("\\", "/"):
            location = (argv[0].replace("\\", "/")).replace("Code/setup.py" , "")

        try:
            import simplejson as json
        except(ModuleNotFoundError):
            import json

        try:
            with open(f"{location}data/mainData.json" , "x") as file:
                file.write("{}")
                file.close()
        except(Exception):
            print("Something went wrong with the mainData.json file")

        try:
            with open(f"{location}data/programs.json" , "x") as file:
                file.write("{}")
                file.close()
        except(Exception):
            print("Something went wrong with the program.json ")


        try:
            with open(f"{location}data/mainData.json", "w") as writable:
                guild_id = input("\nEnter your guild id: ")
                token = input("\nPlease enter bot token: ")
                build = {
                    "guildID" : f"{guild_id}",
                    "token" : f"{token}"
                }

                json.dump(build, writable, indent=3)
                writable.close()
        except(Exception):
            print("Oops something went wrong when trying to write to mainData.json file")

        try:
            with open(f"{location}data/programs.json", "w") as writable:
                build = {"apps": []}
                json.dump(build, writable, indent=3)
        except(Exception):
            pass

    def __createTask(self):

        
        print("If you want DiscordControll to run when you log on follow this link: https://youtu.be/DVUlkU2AxgQ\
             \n\
             \nMake sure to click 'on logon' instead of 'daily'.\
             \nMake sure you enter the path for PCBOT.pyw, NOT THE RELETAIVE PATH or JUST THE NAME.")
        time.sleep(3)

if __name__ == "__main__":
    if platform == "win32":
        setup_win32().run()
        input()
    else:
        print(f"\n ### {platform.capitalize()} is not supported. Please close this window.###\n")
        

	
