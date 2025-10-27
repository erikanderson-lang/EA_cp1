#Eacp1
import random
import time
name = input("What is your name?: ")
time.sleep (1)
print (f"hello {name}.")
time.sleep (1)
playerclass = int(input(f"What class of fighter are you? 1 if you are a Fighter. 2 if you are a Mage. 3 if you are a Rouge. 4 if you are a clown: "))

if playerclass == 1:
    print("""Great, Fighter, here are your stats. 
          Health: 30 
          Defense: 14 
          Attack: 23""")
    playerhealth = 30
    playerdefence = 14
    playerattack = 14

elif playerclass == 2:
    print ("""Great, Mage, here are your stats.
          Health:25 
          Defense: 20
          Attack: 17""")
    playerhealth = 25
    playerdefence = 20
    playerattack = 17

elif playerclass == 3:
    print ("""Great, Rouge, here are your stats. 
          Health:20
          Defense: 20
          Attack: 25""")
    playerhealth = 20
    playerdefence = 20
    playerattack = 25

elif playerclass == 4:
    print ("""Great, clown, here are your stats.
          Health:40
          Defense: 10
          Attack: 10""")
    playerhealth = 40
    playerdefence = 10
    playerattack = 10

elif playerclass == 22:
    print ("""Great E, here are your stats.
          Health:40
          Defense: 40
          Attack: 40""")
    playerhealth = 40
    playerdefence = 40
    playerattack = 40

print(". ")
time.sleep(.5)
print(". ")
time.sleep(.5)
print(". ")
time.sleep(.5)
print(". ")
time.sleep(.5)
print(". ")
time.sleep(.5)
print(". ")
time.sleep(.5)
print(". ")
time.sleep(1.5)
print("oh nein a monster came out from behind a large rock ready to fight you!(dun dun dun)")
time.sleep(.5)
firstturn = random.randint(1,2)
if firstturn ==
print (firstturn)
