ip_address = input("Enter the ip: ")

parts = ip_address.split(".")

valid = True

for part in parts:
    if len(parts) != 4:
        print("Invalid IP! A IP Must have exactly 4 parts!.")
        valid = False
        break
    elif part == "":
        print("Invalid IP! Missing a part!")
        valid = False
        break
    elif int(part) > 255:
        print("Invalid IP, each part must be maximum 255.")
        valid = False
        break
if valid:
    print("Valid IP!")

    print("")
    print("IP Address normal:")
    print(ip_address)
    print("Only numbers IP Address:")
    print(ip_address.replace(".",""))

    print("Qnt of the parts on IP:",len(parts))
    print("Qnt of numbers on IP:",len(ip_address.replace(".","")))
    counting = 0
    for item in parts:
        counting += 1
        print(counting, ".", item)
    print("")

    ip_reverse = ""

    for number in ip_address:
        ip_reverse = number + ip_reverse
    print("IP Address reverse:")
    print(ip_reverse)
    print("Only numbers IP reverse:")
    print(ip_reverse.replace(".",""))

    parts_reverse = ip_reverse.split(".")

    print("Qnt of the parts on IP reverse: ",len(parts_reverse))
    print("Qnt of numbers on IP:",len(ip_reverse.replace(".","")))
    counting = 0
    for item in parts_reverse:
        counting += 1
        print(counting, ".", item)