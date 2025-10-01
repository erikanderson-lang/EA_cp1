#EAcp1 

#What is iteration
#the act of repeating

#How do you write a for loop?
#for num in

#What is the variable that is represented commonly by i?
#iteration

#What can we name that besides i?
#iteration

#Why do we indent on the line after the colon?
#so it all is in the thing

#What is repetition in programming?
#repeting

#How do you write a range function?
#for num in range(1,11,2):


import time

nums = {1,223,3,43,5,6,7,833,9,100,11,12,13,148,15,160,17,18,19,200}

for num in nums:
    num /= 2
    if num>100:
        print(f"{num} is only half of {num*2} ")
    else:
        print (num)
print("the end")


for num in range(1,11,2):  #1-10
    print(num)
    


for num in range(20,0,-2):  
    print(num)
    

print("00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000")
print(" ")
print(" ")
for num in range(10,0,-1):  
    print(num)
    time.sleep(1)