# Author: Glowstudent
# Program: Calculate Miles-Per-Gallon

gallonsUsed: int
milesDriven: int
milesPerGallon: float

milesDriven = input("Enter number of miles driven (round to the nearest mile): ")
gallonsUsed = input("Enter gallons of gas used (round to the nearest gallon): ")
milesPerGallon = (int(milesDriven) / int(gallonsUsed))

print("Estimated miles-per-gallon: {0:.2f}".format(milesPerGallon))
