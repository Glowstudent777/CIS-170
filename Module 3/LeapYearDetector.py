# Author: Glowstudent
# Program: Leap Year Detector

year: int

year = int(input("Enter a year to see if it is a leap year: "))

if (year % 400 == 0):
    print("{0} is a leap year".format(year))
elif (year % 100 != 0 and year % 4 == 0):
    print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))