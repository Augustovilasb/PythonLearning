# The import comando, to import the "time" Python function
import time

# FINAL variables, Value for Month and Year
# Every month counts as 31 days so any day (up to the 31) fits in the month
MONTH = 31
# A year is 12 of these months (12 * 31 = 372) so the months always fit in the year
YEAR = MONTH * 12
# It's the way I found to keep the dates in the correct order and the age correct

# Using the function 'time.strftime' to get the current date for today
# the day is '%d', month is '%m' and year as '%Y', with the upper
# case for Y cause the lower case doesn't give the year date in 4 digits.
current_date = time.strftime("%d/%m/%Y")

# Input to collect the birthday user date
date_birth = input("Please, input your birthday: (dd/mm/yyyy)\n")

# Here is the section where I split the date into, day, month and year (dd/mm/yyyy)
# Also, I am casting the date because the input() and the function time, only return a string
day_birth = int(date_birth[:2])
month_birth = int(date_birth[3:5])
year_birth = int(date_birth[6:10])

day_current = int(current_date[:2])
month_current = int(current_date[3:5])
year_current = int(current_date[6:10])

# Calculation for the total BIRTH date and CURRENT date, in days (year * 372 + month + day
total_days_birth = (year_birth * YEAR) + (month_birth * MONTH) + day_birth
total_days_current = (year_current * YEAR) + (month_current * MONTH) + day_current

# The total number of days the user has been alive
days_alive = total_days_current - total_days_birth
# Where I divide the days alive by the days in one year
# Using '//' to only count the full years
# So, I have the total of the years inside the days alive
age = days_alive // YEAR

# Printing the 'age'
print(f"You are {age} years old!!")

# The conditional 'IF', where I am checking if the user is 17 or older
# If the user is 17 or older, print the message he is able to start the process
# Else he is younger, not able to start the process
if age >= 17:
    print("You are able to start the driving license process.")
else:
    print("You are not able to start the driving license process.")