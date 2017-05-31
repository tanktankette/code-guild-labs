def snake_check(word):
    if "_" in word:
        return True
    return False


def camel_check(word):
    for w in word:
        if w.isupper():
            return True
    return False


word = input("Enter a word: ")
if snake_check(word) and not camel_check(word):
    print("snake_case")
elif camel_check(word) and not snake_check(word):
    print("CamelCase")
else:
    print("???")
