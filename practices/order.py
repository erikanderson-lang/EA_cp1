#EACP1
import time
main = {
    "hamburger plain":54.99,
    "double bacon cheese burgur":10.01,
    "chicken jokey strips":99.99
}

side = {
    "quesadilla":22.22,
    "fries":2.34,
    "salad":19.02,
    " ":0.01
}

drink = {
    "rootbeer":1.22,
    "coke":1.34,
    "american":199.02
}
print(f"hi welcome comerade to the food. Look at menu and choose what you want.")
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

order_main= input("What do you want for main comerade: ")
order_side= input("What do you want for side comerade: ")
order_side2 = input("What do you want for second side comerade: ")
order_drink= input("What do you want for drink comerade: ")
ordre = order_main + order_side + order_side2 + order_drink
00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
print(f"{ordre}")


