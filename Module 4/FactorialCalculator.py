# Author: Glowstudent
# Program: Factorial Calculator

input: int
count: int
max_input = 16

input = int(input("Enter a number less than or equal to 16: "))

while input > max_input:
    input = int(input("Number is too large. Pick a smaller number: "))

count = 1
for i in range(1, input + 1):
    count *= i

print("The factorial of {0} is {1}".format(input, count))
