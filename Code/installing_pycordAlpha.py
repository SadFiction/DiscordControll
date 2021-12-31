import os, sys, time
import webbrowser



def __install_Git():
    webbrowser.open_new("https://github.com/git-for-windows/git/releases/download/v2.34.1.windows.1/Git-2.34.1-64-bit.exe")
    print("------- Please enter save , make sure it is saved in the downloads folder --------")
    input("Press enter to continue...")
    
    
    checking = True

    while checking:
        time.sleep(3)
        
        os.system(f"start C:/Users/{ os.environ.get( 'USERNAME' )}/Downloads/Git-2.34.1-64-bit.exe")
        print("Please download the folowing and make sure to uncheck the GUI element")
        time.sleep(5)
        input_ = input("Just press enter if installed or type 'retry' to try again... ")
        if input_.lower() != "retry":
            checking = False

def __install_pycordAlpha():
    if sys.platform == "win32":
        import subprocess as sp
        sp.run(["powershell", "-Command", "git clone https://github.com/Pycord-Development/pycord; cd pycord; py -m  pip  install . ; "], capture_output=False)
        time.sleep(1)
        os.system("rmdir /s pycord")
        os.system('cls||clear')
        print("--- py-cord --- installed successfully")
    

def install():
    if sys.platform == "win32":
        __install_Git()
    __install_pycordAlpha()

if __name__ == "__main__":
    install()