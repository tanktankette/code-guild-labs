import string

word = input("What word(s) am I checking: ")
for c in string.punctuation:
    word = word.replace(c, "")
word = word.replace(" ", "")

print(reversed(word))
print(word == "".join(reversed(word)))
