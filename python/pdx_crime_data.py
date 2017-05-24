import csv
from os import system
system("clear")

def get_most_common(dictionary):
    most_common_crime = ""
    most_common_crime_num = 0
    print(most_common_crime)
    for i in dictionary.keys():
        if dictionary[i] > most_common_crime_num or most_common_crime == "":
            most_common_crime_num = dictionary[i]
            most_common_crime = i
    return most_common_crime + ": " + str(most_common_crime_num)

def get_least_common(dictionary):
    least_common_crime = ""
    least_common_crime_num = 0
    print(least_common_crime)
    for i in dictionary.keys():
        if dictionary[i] < least_common_crime_num or least_common_crime == "":
            least_common_crime_num = dictionary[i]
            least_common_crime = i
    return least_common_crime + ": " + str(least_common_crime_num)

data = [{}, {}, {}, {}, {}]

files = [\
"./data/crime_incident_data_2011.csv", "./data/crime_incident_data_2012.csv", \
"./data/crime_incident_data_2013.csv", "./data/crime_incident_data_2014.csv", \
"./data/crime_incident_data_recent.csv"]

opened_file = ""

#Import csv files into dictionaries

for i in range(0,5):
    print("Loading " + str(2011+i))
    opened_file = csv.DictReader(open(files[i], "r"))
    for r in opened_file:
        data[i][r["Record ID"]] = r
print("Ready to go")

#Tally crimes by year and as a total

crime = ""
crime_count_by_year = [{}, {}, {}, {}, {}]
crime_count_total = {}

for j in range(0,5):
    for i in data[j].keys():
        crime = data[j][i]["Major Offense Type"]
        if crime in crime_count_by_year[j]:
            crime_count_by_year[j][crime] += 1
        else:
            crime_count_by_year[j][crime] = 1

        if crime in crime_count_total:
            crime_count_total[crime] += 1
        else:
            crime_count_total[crime] = 1

#Analyize data, find biggest year, then most common crime, then least common crime

yearly_totals = [0,0,0,0,0]

for i in range(0,5):
    for j in crime_count_by_year[i].keys():
        yearly_totals[i] += crime_count_by_year[i][j]
    print(f"In {2011 + i} there were {yearly_totals[i]} crimes")

largest = max(yearly_totals)
print (f"The most crime was in {2011 + yearly_totals.index(largest)}")

print("Most common total: " + get_most_common(crime_count_total))
for i in range(0,5):
        print("In " + str(2011+i) + ": " + get_most_common(crime_count_by_year[i]))

print("Least common total: " + get_least_common(crime_count_total))
for i in range(0,5):
        print("In " + str(2011+i) + ": " + get_least_common(crime_count_by_year[i]))



import matplotlib.pyplot as plt

i = 0
chart_values = list(crime_count_total.values())
chart_labels = list(crime_count_total.keys())
while len(chart_values) > 5:
    i = chart_values.index(min(chart_values))
    chart_values.pop(i)
    chart_labels.pop(i)
print(chart_values)


plt.pie(chart_values, labels=chart_labels, autopct='%1.1f%%')
plt.title("5 Most common crimes within the time period")
plt.show()
