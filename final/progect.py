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
    " ": 1,
    " ": 2,
    " ": 3,
    " ": 4
    }
print("security systems active.")
t.sleep(1)
print("you are looting a star cruiser about to sink in to an electrical storm when the security systems went off. you have twenty muinetes. you now need to get out before the ship sinks.")
t.sleep(3)
print("or")
t.sleep(1)
print("the security droids destroy you. either way, you need to leave but first you need to go to the bridge and free the docking bay. time starts now.")
def storeroom():
    choise = int(input("go to hall(1) or loot storage room (2): ").strip())
    if choise == 1:
      pass
    elif choise == 2:
       print (f"you got {r.choice(list(loot.keys()))}.")
    else:
       print ("invalid choise redo")
storeroom()

def hallfight():
    fightrun = int(input("you are in the hall when you find securitydroids closing in. you can run(1) or fight(2): ").strip())
    if fightrun == 1:
        runchance = r.randint(1,2)
        if runchance == 1:
            print("you ran away into other droids who quickly disconected you from the server of life")
        elif runchance == 2:
            print("you got away")
        else:
            print("invalid choise redo")
    elif fightrun == 2:
        print("")


    else:
        print ("invalid choise redo")

def hall():
    hallway = int(input("There are two ways to go left bridge(1) or right to other rooms(2): ").strip())
    if hallway == 1:
        print("you make it to the bridge. You find the consel then words pop up on the screen saying '' ")