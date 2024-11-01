# Author: Glowstudent
# Program: Siblings

input: int


def main():
    global uInput

    uInput = input("Enter number of siblings: ")

    if uInput.isdigit():
        if int(uInput) >= 0:
            if int(uInput) == 0:
                print("Ah you are an only child.")
                exit(0)
            else:
                siblings = [""] * int(uInput)

                for i in range(int(uInput)):
                    siblings[i] = str(
                        input(f"Enter in sibling number {(int(i) + 1)} name: ")
                    )

                print("Your siblings are: ")
                for i in range(int(uInput)):
                    print(siblings[i])

                exit(0)
        else:
            print("Invalid entry for number of siblings! Program is exiting!")
            exit(0)
    else:
        print("Invalid entry for number of siblings! Program is exiting!")
        exit(0)


if __name__ == "__main__":
    main()
