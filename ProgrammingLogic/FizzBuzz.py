number = int(input("Enter a number:"))

for n in range(1, number + 1):

    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuss")
    elif n % 5 == 0:
        print("Buzz")
    elif n % 3 == 0:
        print("Fizz")
    else:
        print(n)