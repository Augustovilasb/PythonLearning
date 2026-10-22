age = int(input("Input your age: "))

if age >= 17:
    hasProvisional = input("Do you have a provisional Licence? (yes or no): ")
    if hasProvisional == "yes":
        print("U are eligible to drive.")
    else:
        print("U are not eligible to drive.")
else:
    print("U are not eligible for a drive licence.")