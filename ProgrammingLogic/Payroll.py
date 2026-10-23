# Until 39 hours = paid €35 per hour
# Each overtime = paid €50 per hour
# Gross = Total paid

# Creating the variables to organize the code
weeks_per_year = 52
max_hours = 39
basic_rate = 35
overtime_rate = 50
low_tax_rate = 0.21
high_tax_rate = 0.42

# Converting the yearly tax limits to weekly values
tax_free_limit = 18000 / weeks_per_year
higher_tax_limit = 49000 / weeks_per_year

# The variable to receive the input from the user
worked_hours = float(input("How many hours did you work last week? "))

# The IF/ELSE to calculate the payment rate
# Where above 39 hours the user receives overtime pay of €50/hour
# Otherwise, the basic rate is €35/hour
if worked_hours <= max_hours:
    basic_payment = worked_hours * basic_rate
    overtime_payment = 0
    gross_pay = basic_payment
else:
    basic_payment = max_hours * basic_rate
    overtime_payment = (worked_hours - max_hours) * overtime_rate
    gross_pay = basic_payment + overtime_payment

# The IF/ELSE to calculate the tax paid on payslip
# IF the gross pay is up to the tax-free limit (346.15 weekly) the user doesn't pay tax.
# ELIF the gross pay is between the low and high limit (942.31 weekly) the user pays 21% only on the amount above the tax-free limit.
# ELSE the gross pay is above the high limit, the user pays 21% on the amount between the two limits plus 42% only on the amount above the high limit.
if gross_pay <= tax_free_limit:
    total_tax = 0
elif gross_pay <= higher_tax_limit:
    total_tax = (gross_pay - tax_free_limit) * low_tax_rate
else:
    total_tax = ((higher_tax_limit - tax_free_limit) * low_tax_rate + (gross_pay  - higher_tax_limit) * high_tax_rate)

# Calculating the Net Pay, which is the payment after tax
# gross pay before tax and net pay after tax
net_pay = gross_pay - total_tax

# Creating the PaySlip layout
# Where I used the ':<22' to define the spaces between the characters and the ':'
# And also I used the ':.2f' to round the final value, because the 'round(...,2)' doesn't show two decimal places
print("")
print("-" * 35)
print("PAYSLIP")
print("-" * 35)
print(f"{'Hours worked':<22}: {worked_hours}")
print(f"{'Standard pay amount':<22}: {basic_payment:.2f}")
print(f"{'Over-time pay amount':<22}: {overtime_payment:.2f}")
print(f"{'Gross Pay':<22}: {gross_pay:.2f}")
print("-" * 35)
print(f"{'Total Tax':<22}: {total_tax:.2f}")
print("-" * 35)
print(f"{'Net Pay':<22}: {net_pay:.2f}")
print("-" * 35)
