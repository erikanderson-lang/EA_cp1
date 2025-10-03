#Ea 1 while loops
import time
import random

#What is a while loop?
#num = 1 
#while num <= 20:
#    print(num)
#    time.sleep(.01)
#    num += 1

#How are while loops different from for loops?
#they make infinite loops

#Why do we need a counter in a while loop?
#so we dont break our computer

#What is a break statement?
#break

#How do we use an else statement with a while loop?
#

#Does a break statement let the else statement happen?
#no

#What does continue do?
#continues the loop

for num in range(1,21):
    print(num)
    time.sleep(.02)

num = 1 
while num <= 20:
    print(num)
    time.sleep(.01)
    num += 1

goose = random.randint(1,20)
count = 1

while True:
    count += 1
    if count == goose:
        break
    else:
        print("duck")
        time.sleep(.1)
else:
    print("goose")

i = 0

#while i <20:
#    if i ==10:
#        print("i is 10")
#        continue
#    else:
#        print(f"{i}E")
#
#print("the end")