# implement a program  that compares three numbers and prints the large one
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
if (num1>num2) and (num1>num3):
    print(num1," is the largest among two numbers.")
elif (num2>num1) and (num2>num3):
    print(num2,"is the largest among two  numbers.")
elif (num3>num1) and (num3>num1):
    print(num3,"is the largest among two numbers.")
else:
    print("The three numbers are equal.")            