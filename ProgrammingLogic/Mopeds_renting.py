# weekend or weekday
# 50cc or 250cc
# 3 hours or more

moped_type = input("Enter the moped type: (50cc, 250cc) ").lower()
day_renting = input("Enter the day: (Weekday or Weekend) ").lower()
hours = float(input("How many hours do you want? "))

weekday_50cc_price_first_hours = 15
weekday_50cc_price_after_first_hours = 2.50
weekend_50cc_price_first_hours = 30
weekend_50cc_price_after_first_hours = 7.50

weekday_250cc_price_first_hours = 25
weekday_250cc_price_after_first_hours = 3.50
weekend_250cc_price_first_hours = 35
weekend_250cc_price_after_first_hours = 8.50

moped_one = "50cc"
moped_two = "250cc"
price_final = 0

if day_renting == "weekday":
    if moped_type == "50cc":

        if hours <= 3:
            price_final = weekday_50cc_price_first_hours
        else:
            price_final = weekday_50cc_price_first_hours + ((hours - 3) * weekday_50cc_price_after_first_hours)
    else:
        if moped_type == "250cc":
            if hours <= 3:
                price_final = weekday_250cc_price_first_hours
            else:
                price_final = weekday_250cc_price_first_hours + ((hours - 3) * weekday_250cc_price_after_first_hours)

else:
    if moped_type == "50cc":

        if hours <= 3:
            price_final = weekend_50cc_price_first_hours
        else:
            price_final = weekend_50cc_price_first_hours + ((hours - 3) * weekend_50cc_price_after_first_hours)
    else:
        if moped_type == "250cc":
            if hours <= 3:
                price_final = weekend_250cc_price_first_hours
            else:
                price_final = weekend_250cc_price_first_hours + ((hours - 3) * weekend_250cc_price_after_first_hours)

print(f"The final price is: {price_final:.2f}")

