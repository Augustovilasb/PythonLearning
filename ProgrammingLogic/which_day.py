days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

currentlyDay = input("Input the day: monday, tuesday, wednesday, thursday, friday, saturday, sunday: ").lower()
key = int(input("days ahead: "))

nextDay = ""

if currentlyDay in days:
    dayIndex = days.index(currentlyDay)
    findingDay = (dayIndex + key) % len(days)
    dayIndex = days[findingDay]
    nextDay = dayIndex
    print(nextDay)
else:
    print("Invalid input")
