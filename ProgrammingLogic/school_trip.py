# if we have more than 10 learners, we need one more teacher
# teachers doest pay

capacity_bus = 49
bus_price = 450
qnt_learner_per_teacher = 10

learners = int(input("How many learners will in this trip? "))
hour_leaving = int(input("What time the bus leave? "))
minutes_leaving = int(input("What minute the bus leave? "))
minutes_on_trip = int(input("How long will be the trip? "))
print("")

print("The quantity learners on this trip?", learners)

quantity_teachers = ((learners + 9) // qnt_learner_per_teacher)
print("The quantity teachers necessary for the trip is:", quantity_teachers)

quantity_places_on_bus = quantity_teachers + learners
print("We are expecting", quantity_places_on_bus, "people on this trip")

quantity_busses = (quantity_places_on_bus + 48) // capacity_bus
print("The quantity busses necessary is:", quantity_busses)

bus_cost = (bus_price * quantity_busses) / learners
print("The price the trip per learner is:", round(bus_cost, 2))

hours_on_trip = minutes_on_trip // 60
minutes_left = minutes_on_trip % 60
print(f"Trip duration {hours_on_trip}:{minutes_left:02}")

hours_leaving_in_minutes = (hour_leaving * 60) + minutes_leaving
total_trip_duration = hours_leaving_in_minutes + minutes_on_trip
hours_arriving = (total_trip_duration // 60) % 24
minutes_arriving = total_trip_duration % 60
print(f"We are expecting arriving at {hours_arriving}:{minutes_arriving:02}")