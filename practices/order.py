#EACP1
import time
#the different options for food
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
#prints the stuff
print(f"hi welcome comerade to the food. Look at menu and choose what you want.")
print(" ")
print(" ")
print(" ")
time.sleep(1)
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
time.sleep(1)
e = (", ")
#takes their order
order_main = input("What do you want for main comerade: ").strip().lower()
if order_main == "hamburger plain" or order_main == "double bacon cheese burgur" or order_main == "chicken jokey strips":
    print("")
else: 
    print("did you look at the order or did you miss spell it comerade.")

order_side= input("What do you want for side comerade: ").strip().lower()
if order_side == "quesadilla" or order_side == "fries" or order_side == "salad" or order_side == " ":
        print("")
else: 
    print("did you look at the order or did you miss spell it comerade.")

order_side2 = input("What do you want for second side comerade: ").strip().lower()
if order_side2 == "quesadilla" or order_side2 == "fries" or order_side2 == "salad" or order_side2 == " ":
        print("")
else: 
    print("did you look at the order or did you miss spell it comerade.")


order_drink= input("What do you want for drink comerade: ").strip().lower()
if order_drink == "rootbeer" or order_drink == "coke" or order_drink == "american":
        print("")
else: 
    print("did you look at the order or did you miss spell it comerade.")

ordre = order_main + e + order_side + e + order_side2 + e + order_drink


print(f"order is {ordre}.")
main["hamburger plain"]


