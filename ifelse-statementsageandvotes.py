#write a program that checks if a number is positive,negative,zero
number = float(input("Enter the number to check: "))
if number > 0:
    print("The given number is a positive number. ")
elif number < 0:
    print("The given number is a negative number. ")
else:
    print("The given number is zero.")
