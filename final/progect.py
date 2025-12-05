#EACP1
import random as r
import time as t
loot = {
    "stimpack": 1,
    "t-47 blaster rifle": 2,
    "m-32 charge weapon": 3,
    "250 marks" : 4,
    "50 marks" : 5,
    "thermal detonator" : 6
    }
stats = {
    "health": 1,
    "wealth": 2,
    "accuracy": 3
    }
invintory = {
    "main hand": 1,
    "back pack slot one": 2,
    "back pack slot two": 3,
    "back pack slot three": 4
    }
print("security systems active.")
t.sleep(1)
print("you are looting a star cruiser about to sink in to an electrical storm when the security systems went off. you have twenty muinetes. you now need to get out before the ship sinks.")
t.sleep(3)
print("or")
t.sleep(1)
print("the security droids destroy you. either way, you need to leave but first you need to go to the bridge and free the docking bay. time starts now.")
choise =  int(input("go to hall(1) or loot storage room (2): "))
if choise == 1:
   print(" ")
elif choise == 2:
    print (f"you got {r.choice(loot.keys())}")
else:
    print ("invalid choise redo")
