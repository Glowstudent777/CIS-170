# Author: Glowstudent
# Program: Slot Machine

import random

again: str
moneyTemp: int = 0
moneyTotal: int = 0
betTemp: int = 0
betTotal: int = 0
slot1: int
slot2: int
slot3: int
isInvalid: bool = True

def printSlots(num):
    if num == 1:
        return "Cherries"
    elif num == 2:
        return "Oranges"
    elif num == 3:
        return "Plums"
    elif num == 4:
        return "Bells"
    elif num == 5:
        return "Melons"
    elif num == 6:
        return "Bars"
    else:
        print("Invalid number.")



def playSlots():
    global moneyTemp
    global moneyTotal
    global betTemp
    global betTotal
    global slot1
    global slot2
    global slot3
    global isInvalid

    while isInvalid:
        betTemp = input("Enter amount to bet: ")
        if betTemp.isdigit():
            betTemp = int(betTemp)
            if betTemp > 0:
                isInvalid = False
            else:
                print("Invalid input. Please enter a positive number.")
        else:
            print("Invalid input. Please enter a positive number.")
    
    isInvalid = True

    slot1 = random.randint(1, 6)
    slot2 = random.randint(1, 6)
    slot3 = random.randint(1, 6)

    print("The slots are spinning...")

    print("| " + printSlots(slot1) + " | " + printSlots(slot2) + " | " + printSlots(slot3) + " |")

    if slot1 == slot2 and slot2 == slot3:
        moneyTemp = betTemp * 3
        print("You won $" + str(moneyTemp) + "!")
    elif slot1 == slot2 or slot2 == slot3 or slot1 == slot3:
        moneyTemp = betTemp * 2
        print("You won $" + str(moneyTemp) + "!")
    else:
        moneyTemp = 0
        print("You won $0.")

    moneyTotal += moneyTemp
    betTotal += betTemp

    betTemp = 0
    moneyTemp = 0


def main():
    print("Welcome to the Slot Machine!")
    
    while True:
        playSlots()

        again = input("Would you like to play again? (y/n): ")
        if again.lower() != "y":
            break

    print("You bet a total of $" + str(betTotal) + " and earned $" + str(moneyTotal) + ".")

if __name__ == "__main__":
    main()