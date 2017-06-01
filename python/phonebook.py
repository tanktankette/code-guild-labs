from os import system
import csv
import requests


def retrieve_contacts(phonebook, key, value, return_as_string=True):
    matches = []
    for k in phonebook.keys():
        if value in phonebook[k][key]:
            matches.append(phonebook[k])
    if matches:
        if return_as_string:
            return convert_dictionaries_to_string(matches)
        else:
            return matches
    else:
        return "No matches found"


def send_message(phonebook):
    search = get_search_type()
    results = retrieve_contacts(phonebook, search,
                                input(f"Search for {search}: ").lower(), False)
    i = 0

    if len(results) == 0:
        print("No results")
    elif len(results) > 1:
        print("More than one result found")
        for c in results:
            print(f"{results.index(c)}: {c}")
        i = int(input("Choose contact: "))

    message = input("Write message:\n")

    number = "+1" + results[0]["number"]
    package = {"To": number, "From": "+14243512633", "Body": message}
    AccountSid = "AC86189c370a1fcca6c3dd11c2fa15ee04"

    file = open("authtoken.txt")
    AuthToken = file.read().strip("\n")

    r = requests.post(f"https://{AccountSid}:{AuthToken}@api.twilio.com/\
    2010-04-01/Accounts/{AccountSid}/Messages.json", data=package)
    print("Sent")


def convert_dictionary_to_string(contact):
    string = ""
    for key in contact:
        if key == "name":
            contact[key] = contact[key].capitalize()
        string += f"{key}: {contact[key]}\n"
    # string += "\n"
    return string


def convert_dictionaries_to_string(contacts):  # confusing name?
    string = ""
    for contact in contacts:
        string += convert_dictionary_to_string(contact) + "\n"
    return string


def set_contact(phonebook, name, number="", note=""):

    if name in phonebook:
        contact = phonebook[name]
        if not number:
            number = contact["number"]
        if not note:
            note = contact["note"]
    phonebook[name] = {"name": name, "number": number, "note": note}


def del_contact(phonebook, name):
    phonebook.pop(name)


def take_command():
    command = -1
    while command == -1:
        try:
            command = int(input("""
********Commands********
1: Search for Contact(s)
2: Add/Update Contact
3: Delete Contact
4: Load Phonebook
5: Save Phonebook
6: Send Message

0: Exit
************************
Input: """))
        except ValueError:
            system("clear")
            print("Error, not a valid input\n")
            continue
        system("clear")
        return command


def get_search_type():
    search = -1

    while search == -1:
        try:
            search = int(input("Search by Name (1), Number (2), or Note(3): "))
        except ValueError:
            system("clear")
            print("Error, not a valid input\n")

    if search == 1:
        return "name"
    elif search == 2:
        return "number"
    elif search == 3:
        return "note"


system("clear")

phonebook = {'kieran': {'name': 'kieran',
                        'number': 8456331959,
                        'note': 'Good code is not written, it\'s re-written.'},
             'lambda': {'name': 'lambda',
                        'number': 8454185633,
                        'note': 'I am a robot.'}}

command = 1
search = ""
file_name = ""
opened_file = ""

while command != 0:
    command = take_command()
    if command == 1:
        search = get_search_type()
        print(retrieve_contacts(phonebook, search,
              input(f"Search for {search}: ").lower()))
    elif command == 2:
        set_contact(phonebook, input("Name: ").lower(),
                    input("Number: "), input("Note: "))
        print("Done")
    elif command == 3:
        del_contact(phonebook, input("Delete contact: ").lower())
    elif command == 4:
        file_name = input("File name: ")
        try:
            opened_file = csv.DictReader(open(file_name, "r"))
        except FileNotFoundError:
            system("clear")
            print("File not found")
            continue
        phonebook = {}
        for r in opened_file:
            phonebook[r["name"]] = r
    elif command == 5:
        file_name = input("File name: ")
        opened_file = csv.DictWriter(open(file_name, "w"),
                                     ["name", "note", "number"])
        opened_file.writeheader()
        for c in phonebook.values():
            opened_file.writerow(c)
    elif command == 6:
        send_message(phonebook)
