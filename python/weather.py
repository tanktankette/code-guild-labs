import requests
from os import system

system("clear")

package = {"APPID": "9c862df5681526994f6c14a975122599"}
c = input("City name or Zip Code: ")
t = ""

f = input("C/F: ").upper()


try:
    c=int(c)
    t = "zip"
except:
    t="q"

package[t] = c
r = requests.post("http://api.openweathermap.org/data/2.5/weather", params=package)
j = r.json()

temp = j["main"]["temp"] - 272.15

if(f == "F"):
    temp = temp*9/5 + 32


system("clear")

print(j["weather"][0]["description"].title())
print(f"The temperature is {temp:.2f} degrees {f}")
