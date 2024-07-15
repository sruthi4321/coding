#create a program that converts hours into minutes, minutes,seconds and hours
def hours_to_minutes_and_seconds(hours):
    total_minutes = hours*60 
    minutes = int(total_minutes )
    seconds = int(total_minutes-minutes)*60
    return minutes, seconds
input_hours = float(input("Enter the number of hours: "))
converted_minutes,converted_seconds = hours_to_minutes_and_seconds(input_hours)
print(f"{input_hours} hours is equal to {converted_minutes} minutes, and {converted_seconds} seconds.")

  