
test_score = int(input("Enter your test score? (0 to 100): "))
your_age = int(input("Input your age: "))

if test_score >= 80 and your_age <= 16:
    print("Excellent.")
elif test_score >= 80:
    print("Good")
else:
    print("Try harder.")