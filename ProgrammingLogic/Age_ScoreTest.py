test_score = int(input("Enter your test score? (0 to 100): "))

score = 80
avg_age = 16

if test_score >= score:
    your_age = int(input("Input your age: "))
    if your_age <= 16:
        print("Excellent.")
    else:
        print("Good.")
else:
    print("Please try harder next time.")


