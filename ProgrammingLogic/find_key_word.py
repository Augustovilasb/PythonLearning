sentence = input("Please type a sentence: ").lower()
word = input("Enter a word: ").lower()

if word in sentence:
    word_index = sentence.index(word)
    print("The word",word,"starts at position:",word_index)
else:
    print("We couldn't find the position of",word,"in the sentence")