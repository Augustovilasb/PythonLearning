word = input("Please find a word: ")
letter = input("Enter a letter: ")

if letter in word:
    letter_index = word.index(letter)
    print("The letter", letter, "is at position: ", letter_index)
else:
    print("The letter", letter, "couldn't be found.")