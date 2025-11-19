#EACP1
#What information does map need?
#a function

#What does map return?
#a list of numbers

#What is a lambda function
#a one line thing

#How does using a lambda function and the map function shorten your code?
#it makes it so I can wright it in one line

numbers = [13,54,24,26,35,65,54,2435,5]
#new_nums = []
#for number in numbers:
#    new_nums.append(number/3)
#    print(new_nums)
def divide(num):
    return num/3
new_nums = map(lambda num: num/3,numbers)
for num in new_nums:
    print(num)

