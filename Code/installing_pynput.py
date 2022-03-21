import sys, os

"""Installs the "pynput" module"""
def install():
    #Checks if the current platform is windows in case this script is run from an outside script
    if sys.platform == "win32":
        try:
            #installs pynput and displays the following message when successful
            os.system("py -m pip install pynput")
            print("---- Pynput has been installed ----")
        except(Exception):
            #returns if module could not install
            return ModuleNotFoundError
    else:
                #return error if platform is not windows
                return Error

if __name__ == "__main__":
    install()
    #installs pynput if script is run directly