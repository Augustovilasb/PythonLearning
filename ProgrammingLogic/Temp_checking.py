count = 0
temperatures = []
rack_temp = ""

while rack_temp.lower() != "done":

    rack_temp = input("Enter the temperature, or type 'Done' to exit: ").lower()

    if rack_temp.lower() != "done":
        try:
            temp_values = float(rack_temp)
            temperatures.append(temp_values)
            count += 1
        except ValueError:
            print("enter a valid input!")
            print("")
print("")

if len(temperatures) == 0:
    print("No temperatures entered.")
else:
    print(count,"Temperatures:",temperatures)
    print("")

    # avg
    total = 0
    for temp in temperatures:
        total += temp
    print("The sum of the temperatures is:",total)
    avg = total / len(temperatures)
    print("The avg of the temperatures is:",avg)
    print("")

    # lowest temperature
    lowest = temperatures[0]

    for temp in temperatures:
        if temp < lowest:
            lowest = temp
    print("The lowest temperature is:",lowest)
    print("")

    # higher temperature
    higher = temperatures[0]

    for temp in temperatures:
        if temp > higher:
            higher = temp
    print("The higher temperature is:",higher)
    print("")

    # temperatures > than 27 degrees
    alerts = 0
    bigger_than = 27

    for temp in temperatures:
        if temp > bigger_than:
            alerts += 1
    print("There are", alerts, "temperatures higher than 27 degrees.")
    print("")
    print("Avg =", avg, ", Lowest temp = ", lowest, ", Higher temp = ", higher, ", Temps higher than 27 = ", alerts)