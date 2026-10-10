
password = input("Enter your password:\n")

upper = 0
lower = 0
digits = 0
symbols = 0

for letter in password:
    if  letter.isupper():
        upper += 1
    elif letter.islower():
        lower += 1
    elif letter.isdigit():
        digits += 1
    else:
        symbols +=1

print(f"Upper:{upper} | Lower:{lower} | Digits:{digits} | Symbols:{symbols}")

if len(password) < 8:
    print("Weak password!")
elif upper >= 2 and lower >= 2 and digits >= 2 and symbols >= 2:
    print("STRONG PASSWORD!")
else:
    print("Medium password!")