try:
    number = int(input("gimme a number: "))
    if number % 2 == 0:
        print("The number", number, "is even!")
    else:
        print("The number", number, "is odd!")
except ValueError:
    print("That's not a number!")