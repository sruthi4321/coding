#  Develop a Mini Calculator using python
first = int(input("Enter first number: "))
operator =input("Enter operator(+ ,-, *, /, %):")
second = int(input("Enter second number: "))
if operator == "+":
    print(first + second)
    print("sum of two numbers. ")
elif operator == "-":
    print(first - second)
    print("Difference of two numbers.")
elif operator == "*":
    print(first * second)
    print("Multiplication of two numbers.")
elif operator == "/":
    print(first / second)
    print("Division of two numbers. ")
elif operator == "%":
    print(first % second)             
    print("Mod of two numbers. ")
else:
    print("Invalid operation.")       