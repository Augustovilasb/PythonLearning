hours = float(input("Enter the amount of hours worked:"))
rate = float(input("Enter your rate: "))


normal_paid = hours * rate # only 40 hrs

bonus_overtime = (hours - 40) * (rate / 2) # calculate the bonus of extra hr

overpaid = normal_paid + bonus_overtime # normal paid + bonus

if hours > 40:
    print(overpaid)
elif hours == 40:
    print(normal_paid)
else:
    print(normal_paid)