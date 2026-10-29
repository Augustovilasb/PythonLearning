import time

currently_month = int(time.strftime("%m"))
month_birth = int(input("Enter your month of birth please: "))

months_left = (month_birth - currently_month) % 12

if months_left == 0:
    print("Your birthday is now!!")
else:
    print(f"We have {months_left} months for your birthday!")