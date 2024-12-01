# Author: Glowstudent
# Program: Hacking Toolbox

from pyfiglet import Figlet
from termcolor import colored

input: int

def displayHeader():
    # 62 characters wide
    figlet = Figlet(font="small")
    header = figlet.renderText("Hacking Toolbox")
    print(colored(header, "magenta"))

def displayMainMenu():
    # 62 - 11 = 51 characters wide
    # 51 / 2 = 25 characters wide on the left and 26 right
    print(colored("=" * 25 + " Main Menu " + "=" * 26, "cyan"))
    print("\n")

    # 99 Has one less space because it is a two digit number and shifts while the others dont and it looks bad :/
    # Probably a better way to do this but I am unfamiliar with python
    print(colored("\t1 ", "light_magenta"), colored(" - Password Cracking", "yellow"))
    print(colored("\t2 ", "light_magenta"), colored(" - Cryptography", "yellow"))
    print(colored("\t99 ", "light_magenta"), colored("- Quit Program", "yellow"))
    print("\n")

def displayPasswordCrackingMenu():
    print("Password Cracking Menu")

def displayCryptographyMenu():
    print("Cryptography Menu")

def generatePasswordList():
    print("Password List")

def encodeROT13():
    print("ROT13")

def decodeROT13():
    print("ROT13")

def main():
    selection: int = -1

    displayHeader()
    displayMainMenu()

    while (selection < 1 or selection > 2) and selection != 99:
        selection = input("Enter Selection: ")

        if selection.isdigit() == False:
            print(colored("Invalid Selection!", "red"))
            selection = -1
        else:
            selection = int(selection)
    
    if selection == 1:
        displayPasswordCrackingMenu()
    elif selection == 2:
        displayCryptographyMenu()
    elif selection == 99:
        print(colored("Goodbye!", "red"))
        exit(0)



if __name__ == "__main__":
    main()
