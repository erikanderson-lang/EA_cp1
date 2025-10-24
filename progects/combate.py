#Eacp1
import random
import time
name = input("What is your name?: ")
time.sleep (3)
print (f"hello {name}.")
time.sleep (3)
playerclass = input(f"What class of fighter are you? 1 if you are a Fighter. 2 if you are a Mage. 3 if you are a Rouge: ")
if playerclass == (1):
    print("""Great, here are your stats! 
          Health: 30 
          Defense: 14 
          Attack: 23""")
elif playerclass == (2):
    print ("""Great, here are your stats! 
          Health:25 
          Defense: 20
          Attack: 17""")
elif playerclass == (3):
    print ("""Great, here are your stats! 
          Health:20
          Defense: 20
          Attack: 25""")

