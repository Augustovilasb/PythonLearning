count = 0

for i in range(5):
    number = int(input("Gimme a number: "))
    if i == 0:
        higher = number
    count += number
    if number > higher:
        higher = number
avg = count / 5

print("Sum:",count)
print("Avg:",avg)
print("Higher:",higher)


