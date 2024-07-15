# write a program that converts temperatute from Fahrenheit to celsius
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit-32)*5/9
    return celsius 
# test the function
fahrenheit = float(input("Enter the temperature in fahrenheit: "))
celsius =  fahrenheit_to_celsius(fahrenheit)
print("temperature in celsius is:", celsius)
