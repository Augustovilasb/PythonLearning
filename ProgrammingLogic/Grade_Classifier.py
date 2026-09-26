try:

    grade = float(input("Please, enter your grade: "))

    if (0 > grade) or (grade > 10):
        print("Invalid grade!")
    elif 9 <= grade <= 10:
        print("Excellent job!")
    elif 7 <= grade:
        print("Good job!")
    elif 5 <= grade <= 6.99:
        print("You got it, but almost!")
    elif 5 > grade:
        print("You did FAIL!")

except ValueError:
    print("That's not a grade!")