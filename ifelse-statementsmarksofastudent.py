#write a program tif a person is eligible for a vote and prints its age
age = int(input("Enter the age of a person to vote: "))
if age>=18:
    print("You are eligible to vote.")
elif  age<18:
    print("You are not eligible to vote. ")
elif age <10:
    print("You are a kid.")    
else:
    print("You are done")         