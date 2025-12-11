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
    "health": 20,
    "wealth": 0,
    "damage": 1
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
start_time = t.perf_counter()
def storeroom():
    choise = int(input("go to hall(1) or loot storage room (2): ").strip())
    if choise == 1:
        pass
    elif choise == 2:
        print (f"you got {r.choice(list(loot.keys()))}.")
        pass
    else:
       print ("invalid choise redo")

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

bridge = 0
engine = 0
def hall():
    hallway = int(input("There are two ways to go left bridge(1) or right to other rooms(2): ").strip())
    if hallway == 1:
        if bridge == 0:
            print("you make it to the bridge. You find the consel then words pop up on the screen saying '' ")
            bridge += int(1)

        else:
            bridgealready = int(input("there is nothing here for you. go to hall(1): "))
            if bridgealready == 1:
                roomchoice = int(input("you are in the hall go to begining store room(1) go to second store room(2) go to engine room(3) or go to hanger(4)" ))
                if roomchoice == 1:
                    storeroom()
                    pass
                elif roomchoice == 2:
                    storeroom2()
                    pass
                elif roomchoice == 3:
                    engineroom()
                    pass
                elif roomchoice == 4:
                    hanger()
                    pass
                else:
                    print ("invalid choise redo")
            else:
                print ("invalid choise redo")
    else:
        print ("invalid choise redo")

storeroom()
hallfight()
hall()
