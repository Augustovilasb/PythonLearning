# Exercise 2 on CA1

# Name & Surname
first_name = input("Please, input your first name: ").lower()
surname = input("Please, input your surname: ").lower()

full_name = first_name.capitalize() + " " + surname.capitalize()
print(f"Your full name: {full_name}\n")

# Checking the PPS Number
pps_number = input("Please, input your PPS Number: ").lower()

# A pps has to be 9 digits length
# A pps must have M & F, both as lasts characters
len_pps = len(pps_number)

if pps_number.__contains__("m") and pps_number.__contains__("f"):
    numbers_pps = pps_number.index("m")
    if pps_number[:numbers_pps].isdigit() and len_pps == 9:
        if pps_number[7] == "m" and pps_number[8] == "f":
            print("It's a valid PPS Number.")
        else:
            print("Must have 'M' and 'F' as last characters")
    else:
        print("Must have enough numbers and 9 length")
else:
    print("It's an Invalid PPS Number.")

print(f"\nLOAN")
interest_rate_5_years = 0.0375
interest_rate_5_to_10_years = 0.0333
interest_rate_10_years = 0.03012

reason_loan = input("Please, could you tell me the reason you want the loan? ")
time_loan = int(input("In how many years would you like to pay the loan? "))
initial_P = float(input("How much would you like to loan? "))

if time_loan <= 5:
    rate_interest = interest_rate_5_years
elif time_loan < 10:
    rate_interest = interest_rate_5_to_10_years
else:
    rate_interest = interest_rate_10_years

future_A = initial_P * (1 + rate_interest) ** time_loan
total_interest = future_A - initial_P
interest = rate_interest * 100

print(f"You will pay as a loan + interesting the total of {future_A:.2f}")
print(f"Only as a interesting you are paying the total of {total_interest:.2f}")
print(f"With the interest rate of {interest:.2f}%")

