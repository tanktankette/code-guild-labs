import requests
from bs4 import BeautifulSoup
from os import system

def parse_file(file):
    for line in file:
        yield (i.strip() for i in line.split("  ") if i != "") #Maybe I should generate dictionary generators instead

def get_file():
    command = 0
    while True:
        system("clear")
        print("""\
        1. Load from computer
        2. Load from internet
        0. Exit""")
        command = int(input("Command: "))
        if command == 0: #Exit
            exit()
        elif command == 1: #Load from computer
            return input("Name of file: ")
        elif command == 2: #Load from internet
            #Get list of .rain files and display them for selection
            r = requests.get("https://or.water.usgs.gov/non-usgs/bes/")
            soup = BeautifulSoup(r.text, "html.parser")
            link_list = []
            for link in soup.find_all('a'):
                l = link.get("href")
                if ".rain" in l:
                    print(l)
                    link_list.append(l)

            print("\nThe chosen file will be downloaded to computer for future access\n")
            selection = ""

            while selection not in link_list:
                selection = input("Choose a file: ")

            r = requests.post("https://or.water.usgs.gov/non-usgs/bes/" + selection)
            r = BeautifulSoup(r.text, "html.parser")
            f = open(selection,"w")
            f.write(r.text)

            return selection


file = open(get_file(),"r")
for i in range(11):
    file.readline()

next_is_total = False
largest = ""
largest_value = 0
target = input("Give me a date to search for (ex: 04-NOV-1998): ").upper()
if target == "":
    target = "04-NOV-1998"

in_target = False
result = "   " + target + " "

file = parse_file(file)

for i in file:
    for s in i:
        if next_is_total:
            if s != "-" and int(s) > largest_value:
                largest = next_is_total
                largest_value = int(s)
            next_is_total = False
        elif len(s) > 5:
            next_is_total = s
            if in_target == True:
                target = ""
                in_target = False
        if in_target == True:
            result = f"{result}{s:^6}"
        if s == target:
            in_target = True

system("clear")
print(f"The rainiest day was {largest} with {str(largest_value/100)} inches of rain")

if target == "":
    print("""
       Each point is in hundredths of an inch of rain

               Daily   Hourly data -->
       Date    Total   0     1     2     3     4     5     6     7     8     9     10    11    12    13    14    15    16    17    18    19    20    21    22    23
-------------------------------------------------------------------------------------------------------------------------------------------------------------------""")
    print(result)
else:
    print("Nothing found for search")
