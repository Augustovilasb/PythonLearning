def check_the_learner_grade(grade):

    if (0 > grade) or (grade > 10):
        return "Invalid grade!"
    elif 9 <= grade <= 10:
        return "Excellent job!"
    elif 7 <= grade:
        return "Good job!"
    elif 5 <= grade:
        return "You got it, but almost!"
    else:
        return "You did FAIL!"

try:
    user_grade = float(input("Please, enter your grade: "))
    result = check_the_learner_grade(user_grade)
    print(result)
except ValueError:
    print("That's not a grade!")