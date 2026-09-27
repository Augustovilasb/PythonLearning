numbers = (input("Gimme a sequence of numbers (Min 10): "))

count = 0

for odd in numbers:
    if int(odd) % 2 == 1:
        count += 1
print(count)

