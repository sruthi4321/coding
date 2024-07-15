#create a program that categorizes a given angle as acute,obtuse or right
a = int(input("Enter the Angle1: "))
b = int(input("Enter the Angle2: "))
c = int(input("Enter the Angle3: "))
s = a+b+c
if s==180:
    if a<90 and b<90 and c<90:
        print("It is an acute angle triangle.")
    elif a==90 or b==90 or c==90:
        print("It is an right angle triangle.")
    else:
        print("It ia an obtuse angle triangle.")
else:
    print("You have entered wrong sets of triangle. ")                