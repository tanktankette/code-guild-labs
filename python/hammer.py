import os


def get_time():
    time_string = ""
    while (time_string.find(":") != 1 or len(time_string) != 4) \
            and (time_string.find(":") != 2 or len(time_string) != 5):
        os.system("clear")
        print("Please enter in 24 hour hh:mm format")
        time_string = input("What time is it: ")

    time_list = time_string.split(":")

    # Should use a try here, in case someone uses anything but digits
    # and more than one colon
    hour = int(time_list[0])
    minute = int(time_list[1])

    if hour < 0 or hour >= 24 or minute < 0 or minute >= 60:
        return -1
    else:
        return hour + minute/60


time_float = -1

while time_float == -1:
    time_float = get_time()

if time_float >= 7 and time_float <= 9:
    print("Breakfast")
elif time_float >= 12 and time_float <= 14:
    print("Lunch")
elif time_float >= 19 and time_float <= 21:
    print("Dinner")
elif time_float >= 22 or time_float <= 4:
    print("Hammer")
else:
    print("Nothing!")

#
# Breakfast: 7AM - 9AM
# Lunch: 12PM - 2PM
# Dinner: 7PM - 9PM
# Hammer: 10PM - 4AM
