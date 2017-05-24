import os

phone_number = ""

while len(phone_number) != 10:
    os.system("clear")
    print("Please enter a 10 digit phone number")
    phone_number = input("Your phone number: ")

phone_number = list(phone_number)
phone_number.insert(0,'(')
phone_number.insert(4,')')
phone_number.insert(5,' ')
phone_number.insert(9,'-')
phone_number = "".join(phone_number)

print(phone_number)
