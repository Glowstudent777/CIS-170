# Author: Glowstudent
# Program: Kilometer Converter

kilometers: float

def kmToMiles(km: float) -> float:
    return km * 0.6214

def main():
    kilometers = float(input("Enter the number of kilometers to convert to miles: "))
    miles = kmToMiles(kilometers)
    print(f"{kilometers} kilometers is approximately {miles:.4g} miles.")

if __name__ == "__main__":
    main()