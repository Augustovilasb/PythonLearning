count = 0
temperatures = []
rack_temp = ""

while rack_temp.lower() != "done":

    rack_temp = input("Enter the temperature, or type 'Done' to exit: ").lower()

    if rack_temp.lower() != "done":
        temp_values = float(rack_temp)
        temperatures.append(temp_values)
        count += 1
    else:
        print("Welcome")
        break

print(count,"Temperatures:",temperatures)