#Ea 1
import time
import random
hang = """|___________
|
|
|___________
|
|
|____________
"""
print (f"{hang}")

print ("this is rock paper scisors comrade. you chose 1 = rock, 2 = paper, or 3 = scisors.")
choise = input("chose 1-3: ")

rock = 1
paper = 2
scissors = 3

compchoise = random.randint(1,3)
for num in range(3,0,-1):
    print(num)
    time.sleep(1)



if compchoise == 1:
    print("I chose rock")

if compchoise == 2:
    print("I chose paper")

if compchoise == 3:
    print("I chose scissors")

if compchoise == choise: 
    print ("We chose same go again")
    continue