# Until 39 hours = paid 35 hour
# Each overtime = pais 50 hour
# Gross = Total paid

max_hours = 39
basic_rate = 35
overtime_rate = 50

worked_hours = float(input("How many hours did you worked last week? "))

if worked_hours <= max_hours:
    basic_payment = worked_hours * basic_rate
    overtime_payment = 0
    gross_pay = basic_payment
    print(f"Will you receive {basic_payment} this week.")
elif worked_hours > max_hours:
    basic_payment = max_hours * basic_rate
    overtime_payment = (worked_hours - max_hours) * overtime_rate
    gross_pay = basic_payment + overtime_payment
    print(f"Will you receive {gross_pay} this week.")

tax_free_limit = 18000 / 52
higher_tax_limit = 49000 / 52
print(round(tax_free_limit, 2))
print(round(higher_tax_limit, 2))