phrase = (input("Gimme a sentence (Min 10 letters): ").lower())

count = 0

for letter in phrase:
    if letter in {"a","e","i","o","u"}:
        count += 1
print(count)
