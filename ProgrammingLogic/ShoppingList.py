
print("Welcome, u can type 'leave' to exit anytime")

order = ""
count = 0
items = []

while order != "leave":
    order = input("Would u like anything? ").lower().replace(" ", "")
    if order != "leave":
        if order in items:
            print("It's double!")
        elif order == "":
            print("U must type an item!")
        elif order == "remove":
            print("U are in 'Remove mode'")
            rmv = input("Peak an item to remove: ")
            items.remove(rmv)
            count -= 1
        else:
            count += 1
            items.append(order)

print("U have ",count,"items.")

counting = 0
for item in items:
    counting += 1
    print(counting,".",item)