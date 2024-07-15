# python program to check whether the string is a  palindrome or not
str = input("Enter a string to check: ")
r = ""
for i in str:
    r = i+r
if (str==r):
    print("It is a palidrome.")
else:
    print(" It is not a palidrome.")    