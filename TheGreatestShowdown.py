# Task 1
number1 = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))
number3 = int(input("Enter one more number: "))

if number1 > number2 and number1 > number3:
    print("The first number is the greatest.")
elif number2 > number1 and number2 > number3:
    print("The second number is the greatest.")
else:
    print("The third number is the greatest.")

# Task 2
number1 = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))
number3 = int(input("Enter one more number: "))

if number1 < number2 and number1 < number3:
    print("The first number is the smallest.")
elif number2 < number1 and number2 < number3:
    print("The second number is the smallest.")
else:
    print("The third number is the smallest.")