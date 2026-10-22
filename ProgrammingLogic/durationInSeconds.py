# Create a program to read values representing a time duration; in hours, minutes, and seconds,
# and then print the equivalent total number of seconds.

# Asking the hour input
hour = int(input("Please input the hour, int 24h: "))
print(hour)
minutes = int(input("Please input the minutes: "))
print(minutes)
seconds = int(input("Please input the seconds: "))
print(seconds)
print("")
print("The exactly time is:")
print(f"{hour}h {minutes}m {seconds}s")
print("")

print("Calculating total of minutes")
totalMinutes = int((hour * 60) + minutes)
print("The total of minutes:", totalMinutes,"minutes")
print("")
print("Calculating total of seconds")
totalSeconds = int((totalMinutes*60) + seconds)
print("The total of seconds:", totalSeconds,"seconds")
print("")