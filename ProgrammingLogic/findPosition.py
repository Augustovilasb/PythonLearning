msg = input("Please input the text: ")
letter = input("Please input the letter: ")

letter_index = msg.index(letter)
print("The index of letter", letter, "is: ",  letter_index)

for letter_index in range(len(msg)):
    if msg[letter_index] == letter:
        print("Found at position", letter_index)
