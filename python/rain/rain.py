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

in_target = False
result = ""

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
                in_target = False
        if s == target:
            in_target = True
        if in_target == True:
            result = result + s + "\t"
system("clear")
print(f"The rainiest day was {largest} with {str(largest_value/100)} inches of rain")

if result == "":
    print("Nothing found for search")
else:
    print("""
       Each point is in hundredths of an inch of rain
       
       \t\tDaily\tHourly data -->
       Date\tTotal\t0\t1\t2\t3\t4\t5\t6\t7\t8\t9\t10\t11\t12\t13\t14\t15\t16\t17\t18\t19\t20\t21\t22\t23
    ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------""")
    print(result)
