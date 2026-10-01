statuses = ["up", "up", "down", "up"]

rack_ok = True

for status in statuses:
    print(status)
    if status == "down":
        rack_ok = False
print("")
print(rack_ok)