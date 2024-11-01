# Author: Glowstudent
# Program: Siblings

input: int


def main():
    global input

    input = input("Enter number of siblings: ")

    if input.isdigit():
        if int(input) >= 0:
            if int(input) == 0:
                print("You are an only child.")
                exit(0)
            else:
                print("You have", input, "siblings.")
                exit(0)
        else:
            print("Invalid entry for number of siblings! Program is exiting!")
            exit(0)
    else:
        print("Invalid entry for number of siblings! Program is exiting!")
        exit(0)


if __name__ == "__main__":
    main()
