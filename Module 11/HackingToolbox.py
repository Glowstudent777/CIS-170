# Author: Glowstudent
# Program: Hacking Toolbox

from pyfiglet import Figlet
from termcolor import colored

input: int

def clearScreen():
    print("\033[H\033[J")

def centerText(text: str, width: int, fill: str = " "):
    if len(text) >= width:
        return text
    else:
        padding = width - len(text)
        leftPadding = padding // 2
        rightPadding = padding - leftPadding

        return fill * leftPadding + text + fill * rightPadding

def displayHeader():
    # 62 characters wide
    figlet = Figlet(font="small")
    header = figlet.renderText("Hacking Toolbox")
    print(colored(header, "magenta"))

# print() is used to add a blank line, print("\n") does 2 blank lines for some reason
def displayMainMenu():
    print(colored(centerText(" Main Menu ", 62, "="), "cyan"))
    print()
    print(colored("\t1 ", "light_magenta"), colored(" - Password Cracking", "yellow"))
    print(colored("\t2 ", "light_magenta"), colored(" - Cryptography", "yellow"))
    print(colored("\t99 ", "light_magenta"), colored("- Quit Program", "yellow"))
    print()

def displayPasswordCrackingMenu():
    print(colored(centerText(" Password Cracking Menu ", 62, "="), "cyan"))
    print()
    print(colored("\t1 ", "light_magenta"), colored(" - Generate a wordlist", "yellow"))
    print(colored("\t99 ", "light_magenta"), colored("- Return to Main Menu", "yellow"))
    print()

def displayCryptographyMenu():
    print(colored(centerText(" Cryptography Menu ", 62, "="), "cyan"))
    print()
    print(colored("\t1 ", "light_magenta"), colored(" - Decode ROT 13", "yellow"))
    print(colored("\t2 ", "light_magenta"), colored(" - Encode ROT 13", "yellow"))
    print(colored("\t99 ", "light_magenta"), colored("- Return to Main Menu", "yellow"))
    print()

def generatePasswordList(filename: str, prefix: str):
    outFile = open(filename, "w")

    print()
    print("Generating password list...")

    for i in range(10000):
        outFile.write(prefix + str(i).zfill(4) + "\n")
    outFile.close()

    print("Password list generated and saved to", filename)
    print()
    print("Press Enter to return to the Main Menu")
    input()
    main()

def rot13(msg: str):
    result = ""

    for char in msg:
        if char.isalpha():
            asciiValue = ord(char)
            asciiValue += 13

            if char.islower():
                if asciiValue > ord("z"):
                    asciiValue -= 26
            else:
                if asciiValue > ord("Z"):
                    asciiValue -= 26

            result += chr(asciiValue)
        else:
            result += char

    return result

def main():
    selection: int = -1

    print("\033]0;Hacking Toolbox\007")
    clearScreen()
    displayHeader()
    displayMainMenu()

    while (selection < 1 or selection > 2) and selection != 99:
        selection = input("Enter Selection: ")

        if (selection.isdigit() == False) or ((int(selection) < 1 or int(selection) > 2) and int(selection) != 99):
            print(colored("Invalid Selection!", "red"))
            selection = -1
        else:
            selection = int(selection)
    
    if selection == 1:
        filename: str
        prefix: str

        selection = -1

        clearScreen()
        displayHeader()
        displayPasswordCrackingMenu()

        while selection != 1 and selection != 99:
            selection = input("Enter Selection: ")

            if (selection.isdigit() == False) or (int(selection) != 1 and int(selection) != 99):
                print(colored("Invalid Selection!", "red"))
                selection = -1
            else:
                selection = int(selection)
        
        if selection == 1:
            print()
            filename = input("Enter filename to store passwords to: ")

            while filename == "":
                print(colored("Filename cannot be blank!", "red"))
                filename = input("Enter filename to store passwords to: ")

            prefix = input("Enter prefix for password: ")
            generatePasswordList(filename, prefix)
        elif selection == 99:
            main()

    elif selection == 2:

        selection = -1

        clearScreen()
        displayHeader()
        displayCryptographyMenu()

        while (selection < 1 or selection > 2) and selection != 99:
            selection = input("Enter Selection: ")

            if (selection.isdigit() == False) or ((int(selection) < 1 or int(selection) > 2) and int(selection) != 99):
                print(colored("Invalid Selection!", "red"))
                selection = -1
            else:
                selection = int(selection)
            
        if selection == 1:
            decoded: str

            print()
            msg = input("Enter message to decode: ")

            while msg == "":
                print(colored("Message cannot be blank!", "red"))
                msg = input("Enter message to decode: ")

            decoded = rot13(msg)
            print("Decoded message is:", decoded)
            print()
            print("Press Enter to return to the Main Menu")
            input()
            main()
        elif selection == 2:
            encoded: str

            print()
            msg = input("Enter message to encode: ")

            while msg == "":
                print(colored("Message cannot be blank!", "red"))
                msg = input("Enter message to encode: ")

            encoded = rot13(msg)
            print("Encoded message is:", encoded)
            print()
            print("Press Enter to return to the Main Menu")
            input()
            main()
        elif selection == 99:
            main()
    elif selection == 99:
        print(colored("Goodbye!", "red"))
        exit(0)

if __name__ == "__main__":
    main()
