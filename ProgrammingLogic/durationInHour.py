# Write a program that reads a numerical value representing a number of seconds. Calculate and
# print the equivalent amount of time in hours, minutes, and seconds. (reverse of Exercise 1)

# Asking the hour input
seconds = int(input("Please input a numerical number value for seconds: "))
print("The value in seconds is: ",seconds)
print("")

minutesTime = seconds // 60
secondsRemainders = seconds % 60

hoursTime = minutesTime // 60
minutesRemainders = minutesTime % 60

print(f"{seconds} seconds is: {hoursTime}h {minutesRemainders}m {secondsRemainders}s")
