from aifc import Error
import os, time, sys

"""installs the "simplejson" module"""
def install():
        #Checks if the current platform is windows in case this script is run from an outside script
        if sys.platform == "win32":
                try:
                        #installs simple json and displays the following message when successful
                        os.system("py -m pip install simplejson")
                        print("---- successful simplejson has installed ----")
                        time.sleep(5)
                except(Exception):
                        #returns if module could not install
                        return ModuleNotFoundError
        else:
                #return error if platform is not windows
                return Error

if __name__ == "__main__":
        install()
        #installs simplejson if script is run directly
