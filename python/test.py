# trip_miles = int(input("How many miles was this trip? "))
# mpg = float(input("How many miles to the gallon does your get get? "))
# gas_cost = float(input("How much money is a gallon of gas? "))
#
# trip_cost = (trip_miles / mpg) * gas_cost
#
# print(f"Your trip will cost ${trip_cost:.2f}")

# s = bytearray("This is a test","ascii")
# o=""
#
# for c in s:
#     c = bin(c)
#     l = list(c)
#     l.pop(1)
#     o = o+"".join(l)
#
# print(o)

import io
file = open("test.txt","a")
file.write("test\n")
