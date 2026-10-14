price_parking = 2.50
minutes = 60

print("We do have some rules, price 2.50 a hour, if u stay 2h and 15 min, will pay 3 full hrs.")

hour_enter = int(input("Type the hour (00-24) u enter in the park station: "))
minutes_enter = int(input("Type the minutes (0-59) u enter in the park station: "))
hour_leave = int(input("Type the hour (00-24) u leave in the park station: "))
minutes_leave = int(input("Type the minutes (0-59) u leave in the park station: "))

print("You entered in the park station at:", hour_enter, ":",minutes_enter)
print("You leave the park station at:", hour_leave, ":",minutes_leave)

time_start = (hour_enter * 60) + minutes_enter
time_finished = total_in_minutes = (hour_leave * 60) + minutes_leave

total_minutes_parking = time_finished - time_start
total_hours_parking = (total_minutes_parking + 59) // 60
print(total_hours_parking)

hours_charged = total_minutes_parking // 60
minutes_charged = total_minutes_parking % 60
print("Will be charged on", total_hours_parking, "for the parking time")
print("In total u stayed", hours_charged, "h and",minutes_charged,"min" )

final_price = price_parking * total_hours_parking
print("Will be charged on", round(final_price, 2), "Euros for the parking time")

