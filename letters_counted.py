
# To improve your control flow statement skill and dictionary knowledge.
# Count the number of each letter in a sentence.
# collect the letters/chars as a key and the counted numbers as a value in a dictionary.
# Do not use try - except block.

sentence = input("Enter a sentence to calculate the number of letter: ").lower()
num_letter = len(sentence)
count_letter = dict()

for i in sentence:
    count_letter[i] = count_letter.get(i, 0) + 1
print("The number of letters in your sentence is: ", num_letter)
print("Key-value pairs for the numbers of letters is: ", count_letter)