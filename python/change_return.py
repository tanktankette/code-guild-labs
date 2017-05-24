from os import system

def set_til():
    til = [0,0,0,0,0]
    til[0] = int(input("How many dollars in the til: "))
    til[1] = int(input("How many quarters in the til: "))
    til[2] = int(input("How many dimes in the til: "))
    til[3] = int(input("How many nickels in the til: "))
    til[4] = int(input("How many pennies in the til: "))
    return til

def update_til(change, til):
    # Doesn't look to see if there are enough quarters to cover when there aren't
    # enough dollars or nickels for dimes and so on
    if change[0] <= til[0] and change[1] <= til[1] and change[2] <= til[2] \
    and change[3] <= til[3] and change[4] <= til[4]:
        til[0] -= change[0]
        til[1] -= change[1]
        til[2] -= change[2]
        til[3] -= change[3]
        til[4] -= change[4]
        return True
    else:
        return False

def print_change_and_til(change, til):
    if update_til(change, til):
        system("clear")

        print(f"""Expressed in the fewest amount of bills and coins, you have {change[0]} dollars
    {change[1]} quarters, {change[2]} dimes, {change[3]} nickels, and {change[4]} pennies.\n""")
        print(f"""There are {til[0]} dollars, {til[1]} quarters, {til[2]} dimes,
    {til[3]} nickels, and {til[4]} pennies left in the til\n""")
        return True

    else:
        system("clear")
        print("Not enought money in the til")
        return False

def get_change(total, til):

    change = [0,0,0,0,0]

    change[0] = int(total / 100)
    total -= change[0] * 100
    change[1]= int(total / 25)
    total -= change[1] * 25
    change[2]= int(total / 10)
    total -= change[2] * 10
    change[3]= int(total / 5)
    total -= change[3] * 5
    change[4] = int(total / 1)
    total -= change[4] * 1

    return print_change_and_til(change,til)

###PROGRAM START###

system("clear")
til = set_til()
ch = int(float(input("How much is the total: "))*100)

while get_change(ch, til): #Runs until there isn't enough money in til
    ch = int(float(input("How much is the total: "))*100)
