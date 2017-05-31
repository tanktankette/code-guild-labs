from os import system

system("clear")

print("The word should contain at least an 'e' and an 'i'")
word = input("What word am I checking: ")

system("clear")
print(word.capitalize())

i, e, c = 0, 0, 0

if word.count("i") > 0:
    i = word.index("i")
if word.count("e") > 0:
    e = word.index("e")
if word.count("c") > 0:
    c = word.index("c")

if i == 0 or e == 0:
    print("Come back when you can read instructions -.-")
elif i < e:
    print("So i is before e...")
    if c != 0 and c < i:
        print("But they come after c, exception!")
    else:
        print("And there isn't a c beforehand, it fits the rule!")
else:
    print("Hmm, e is before i")
    if c != 0 and c < i:
        print("But there is a c before that, so it fits the rule!")
    else:
        print("There doesn't seem to be a c before that either, exception!")
