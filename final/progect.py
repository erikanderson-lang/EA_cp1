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
print("you are looting a star cruiser about to sink in to an electrical storm when the security systems went off. you now need to get out before the ship sinks.")
t.sleep(3)
print("or")
t.sleep(1)
print("the security droids destroy you. either way, you need to leave but first you need to go to the bridge and free the docking bay. ")
def lootthing(): 
    print(f"you got {r.choice(list(loot.keys()))}.")


def storeroom():
    choise = int(input("go to hall(1) or loot storage room (2): ").strip())
    if choise == 1:
        pass
    elif choise == 2:
        lootthing()
        pass
    else:
       print ("invalid choise redo")

def hallfight():
    fightrun = int(input("you are in the hall when you find securitydroids closing in. you can run(1) or fight(2): ").strip())
    if fightrun == 1:
        runchance = r.randint(1,2)
        if runchance == 1:
            print("you ran away into other droids who quickly disconected you from the server of life")
            print("you died redo")
            t.sleep(12345678)
        elif runchance == 2:
            print("you got away")
        else:
            print("invalid choise redo")
    elif fightrun == 2:
        print("not done yet")
        pass
        
    else:
        print ("invalid choise redo")


def bridge():
    if 0 == 0:
        print("you make it to the bridge. You find the consel then words pop up on the screen saying")
        print("not done yet")
    
        

    else:
        print("there is nothing here for you. go to hall")
        hall()


def storeroom2():
    choise = int(input("go to hall(1) or loot storage room (2): ").strip())
    if choise == 1:
        pass
    elif choise == 2:
        print (f"you got {r.choice(list(loot.keys()))}.")
        pass
    else:
       print ("invalid choise redo")

def engineroom():
    if 0 == 0:
        print("you make it to the engine room. You find the consel then words pop up on the screen saying")
        print("not done yet")
        
    else:
        print("there is nothing here for you. go to hall")
        hall()

def hanger():
    print("not done yet")
    

def hall():
        roomchoice = int(input("you are in the hall go to begining store room(1) go to second store room(2) go to engine room(3) or go to hanger(4): ").strip())
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

storeroom()
hallfight()
while 1<2:
    hall()

