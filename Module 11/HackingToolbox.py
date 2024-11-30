# Author: Glowstudent
# Program: Hacking Toolbox

input: int

def displayHeader():
    print("Header")

def displayMainMenu():
    print("Main Menu")

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
    displayHeader()
    displayMainMenu()
    displayPasswordCrackingMenu()
    displayCryptographyMenu()
    generatePasswordList()
    encodeROT13()
    decodeROT13()

if __name__ == "__main__":
    main()
