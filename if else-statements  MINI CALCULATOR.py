#  Develop a program pizza delivery
print("Welcome to Domino's Pizza deliveries !")
size = input("What size of pizza do you want? Small, Medium, Large: ")
Toppings = int(input("How many toppings do you want? "))
Add_Pepperoni = input("Do you want to add pepperoni? YES or NO: ")
Add_Cheese = input("D0 you want to add cheese? YES or NO: ")
Add_chicken = input("Doyou want to add chicken? YES or NO: ")
Add_spinach = input("Do you want to add spinach? YES or NO: ")
Add_Mushroom = input("D0 you want to add mushroom? YES or NO: ")
bill = 0
if size == "Small":
    bill += 15
elif size == "Medium":
    bill += 20
else:
    bill += 25


if  Add_spinach == "YES":
    if size == "Small":
        bill += 2
    else:
        bill += 3    
if Add_Pepperoni == "YES":
    if size == "Small":
        bill += 2
    else:
        bill  += 3    
if Add_Cheese == "YES":
    if size == "Small":
        bill += 1
    else:
        bill += 1    
if Add_chicken  == "YES":
    if size == "Small":
        bill +2 
    else:
        bill += 2    
if Add_Mushroom  == "YES":
    if size == "Small":
        bill += 2
    else:
        bill += 1    
    print(f" Your final bill is: ${bill}.")     

                       

            

