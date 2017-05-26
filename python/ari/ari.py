from os import system
import string

ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

system("clear")

file_name = input("Name of file: ")

book = open(file_name,"r")
print("Reading, please wait.")
book = book.read()

word_count = book.count("--")
sentence_count = book.count(".")
character_count = 0

print(book.count(". "))

i = 0

for c in string.punctuation:
    word_count += book.count(c + " ")
    word_count += book.count(c + "\n")

for c in string.ascii_lowercase:
    character_count += book.count(c)
    word_count += book.count(c + " ")
    word_count += book.count(c + "\n")
    sentence_count += book.count(c + ".")

for c in string.ascii_uppercase:
    character_count += book.count(c)
    word_count += book.count(c + " ")
    word_count += book.count(c + "\n")

print(character_count, word_count, sentence_count)

index = 4.71*(character_count/word_count) + .5*(word_count/sentence_count) - 21.43
index = int(index + .99)

ari_index = index
if ari_index > 14:
    ari_index = 14

grade = ari_scale[ari_index]["grade_level"]
age = ari_scale[ari_index]["ages"]

print(f"""\
--------------------------------------------------------

The ARI for the file, {file_name}, is {ari_index}.
This corresponds to a {grade} level of difficulty
that is suitable for an average person {age} years old.

--------------------------------------------------------
""")
