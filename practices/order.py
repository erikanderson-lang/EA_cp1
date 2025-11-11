#EACP1
import time
main = {
    "hamburger plain":54.99,
    "double bacon cheese burgur":1.01,
    "CHICKEN JOKEY STRIPS":99.99
}

side = {
    "quesadilla":22.22,
    "fries":2.34,
    "salad":199.02,
    "":0.01
}

drink = {
    "rootbeer":2.22,
    "coke":2.34,
    "american":199.02
}
print("hi welcome comerade to the food. Look at menu and choose what you want.")
print(" ")
print(" ")
print(" ")
time.sleep(7)
print("MAIN")
print(" ")
for key in main.keys():
    print(f"{key} is {main[key]}")
print(" ")
time.sleep(1)
print("SIDES")
print(" ")
for key in side.keys():
    print(f"{key} is {side[key]}")
print(" ")
time.sleep(1)
print("DRINKS")
print(" ")
for key in drink.keys():
    print(f"{key} is {drink[key]}")

print(" ")
print(" ")
print(" ")
time.sleep(7)
input("What do you want comerade: ")