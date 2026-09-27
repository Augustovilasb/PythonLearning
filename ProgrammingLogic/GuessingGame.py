import random

try:

    numbers = list(range(1, 101))
    rnd = random.choice(numbers)

    number = 0

    while number != rnd:
        number = int(input("Try again, between 1 and 100: "))
        if number < 1 or 100 < number:
            print("It's out of the range!")
        elif number < rnd:
            print("Too low!!")
        elif number > rnd:
            print("Too high!")
        else:
            print("U got it!!")

except ValueError:
    print("That's not a number!!")