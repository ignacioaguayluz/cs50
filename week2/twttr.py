vowels = "aeiouAEIOU"

user = input("Input: ")
word = ""

for letter in user:
    if letter not in vowels:
        word += letter

print("Output:", word)