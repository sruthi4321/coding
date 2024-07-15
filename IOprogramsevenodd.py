#create a program that converts seconds into hours,minutes and seconds
def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) //60
    seconds = (seconds % 3600) % 60
    return hours, minutes, seconds
input_seconds = int(input("Enter the number of seconds "))
hours, minutes, seconds = convert_seconds(input_seconds)
print(f"{input_seconds} seconds is equal to {hours} hours, {minutes} minutes, and {seconds} seconds.")

  