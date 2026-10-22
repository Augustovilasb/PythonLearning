grade_percentage = float(input("Please, input the grade in %: "))

# grade table in % (lower limit)
A = 80
B_PLUS = 70
B = 60
B_MINUS = 55
C_PLUS = 50
C = 40
D = 35

while grade_percentage < 0 or grade_percentage > 100:
    print("The grade must be between 0 and 100.")
    grade_percentage = float(input("Please, input the grade in % again: "))

if grade_percentage >= A:
    print(f"The grade of {grade_percentage} is an A.")
elif grade_percentage >= B_PLUS:
    print(f"The grade of {grade_percentage} is a B+.")
elif grade_percentage >= B:
    print(f"The grade of {grade_percentage} is a B.")
elif grade_percentage >= B_MINUS:
    print(f"The grade of {grade_percentage} is a B-.")
elif grade_percentage >= C_PLUS:
    print(f"The grade of {grade_percentage} is a C+.")
elif grade_percentage >= C:
    print(f"The grade of {grade_percentage} is a C.")
elif grade_percentage >= D:
    print(f"The grade of {grade_percentage} is a D.")
else:
    print(f"The grade of {grade_percentage} is an F.")
