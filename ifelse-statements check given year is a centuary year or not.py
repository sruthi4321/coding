#create  a program that determines if a triangle is equilateral , isosceles or scalene
a = float(input("Enter the length of a side a: "))
b = float(input("Enter the length of a side b: "))
c = float(input("Enter the length of a side c: "))
if a == b == c:
    print("It ia a equilateral triangle")
elif  a == b or b == c or a == c:
    print("It is an isosceles triangle. ")
else:
    print("It is an scelene triangle. ")        