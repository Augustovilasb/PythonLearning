# Loan for a Car finance

# Checking the name
first_name = input("Please, enter your first name: ").lower()
second_name = input("Please, enter your surname: ").lower()
name_initials = first_name[0].upper() + "." + second_name[0].upper() + "."

while not first_name.isalpha() or not second_name.isalpha():
    if not first_name.isalpha():
        print("Invalid name format. (Type only letters, please)")
        first_name = input("Please, enter your first name: ").lower()
    elif not second_name.isalpha():
        print("Invalid name format. (Type only letters, please)")
        second_name = input("Please, enter your surname: ").lower()

# Checking the PPS Number
pps_valid = False
pps_number = ""

while not pps_valid:
    pps_number = input("Please, input your PPS Number: ").upper()
    pps_first_part = pps_number[:7]
    pps_second_part = pps_number[7:]

    if 8 <= len(pps_number) <= 9:
        if pps_first_part.isdigit() and pps_second_part.isalpha():
            if pps_second_part[0] == "R" and pps_second_part[1] == "A":
                pps_valid = True
            else:
                print("Invalid Pps Number")
        else:
            print("Invalid Pps Number")
    else:
        print("Invalid Pps Number.")

# Checking the credit score
# Formula = A = P(1 + r/n) ^ (n × t)

N = 12
rate_700 = 0.055
rate_600 = 0.079
rate = 0

credit_score_valid = False
credit_score = ""

while not credit_score_valid:
    credit_score = input("Please, input your credit score (100/900): ")
    higher_score = 900
    middle_score = 700
    lower_score = 600
    limit_min_score = 100

    if credit_score.isdigit():
        credit_score = int(credit_score)
        if limit_min_score <= credit_score <= higher_score:
            credit_score_valid = True
            if credit_score >= middle_score:
                rate = rate_700
            elif credit_score >= lower_score:
                rate = rate_600
            else:
                rate = 0
        else:
            print("Invalid input")
    else:
         print("Invalid input")

if rate > 0:
    price_finance = float(input("Enter the value you would like to finance: "))
    time_years = int(input("Enter how many years would you like to pay: "))
    number_payments = N * time_years

    A = price_finance * (1 + rate/N) ** number_payments
    interesting_paying = A -price_finance
    monthly_payment = A / number_payments

    print("")
    print("*" * 41)
    print("*\t\t\tCar Finance Summary\t\t\t*")
    print("*" * 41)
    print(f"{'Costumer':<18}: {name_initials}")
    print(f"{'PPS Number':<18}: {pps_number}")
    print(f"{'Credit Score':<18}: {credit_score}")
    print(f"{'Finance Term':<18}: {time_years}")
    print(f"{'Finance Amount':<18}: €{price_finance:.2f}")
    print("*" * 41)
    print(f"{'Total amount to be paid':<18}: €{A:.2f}")
    print(f"{'Total interest on finance':<23}: €{interesting_paying:.2f}")
    print(f"{'Total monthly payment':<23}: €{monthly_payment:.2f}")
    print("*" * 41)
else:
    print("You are not able to request a loan.")