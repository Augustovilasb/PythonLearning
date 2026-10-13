servers_names = []
servers_usage = []
name_input = ""
count = 0

while name_input.lower() != "done":
    name_input = input("Server name (or 'done' to finish): ")

    if name_input.lower() != "done":

        valid = False

        while not valid:
            usage_text = input("Server usage in % (0-100): ")
            try:
                usage_input = float(usage_text)
                if usage_input >= 0 and usage_input <= 100:
                    valid = True
                else:
                    print("Please enter a value between 0 and 100.")
            except ValueError:
                print("Please enter a numeric value.")

        servers_names.append(name_input)
        servers_usage.append(usage_input)
        count += 1
        print("")

print(servers_names)
print(servers_usage)