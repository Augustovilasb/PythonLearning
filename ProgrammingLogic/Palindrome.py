word = input("gimme any word: ").lower()
inverse = ""

for letter in word:
    inverse = letter + inverse
print(inverse)

if word == inverse:
    print("It's a palindrome!")
else:
    print("It's not a palindrome!")