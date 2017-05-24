from random import randrange

dice_num = int(input("Number of dice: "))
dice_sides = int(input("How many sides do the dice have: "))
total = 0

for i in range(0,dice_num):
    total += randrange(1,dice_sides+1)

print(total)
