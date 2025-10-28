#EA

#what is the porpous of a function?
#they organise your code and make it reuseable

#How do you wrght functions?
#def add(x,y):
#    print(f"{x}+{y} = {x+y}")

#Why shoud functions be abstract?
#so it can be reuseable

#how do you increce the readability of program?
#add functions

#what does the modularity have to do with functions?
#makes it simpeler 

#how do arguments and parameters work togather?
#by working togather

#what are return statements? what do they do?
#they replace the call with the answer


def add(x,y):
    print(f"{x}+{y} = {x+y}")

def add(x,y):
    return x+y

add(5,5)
print(f"10 + 72 = {add(10,72)}")
x = 0
while x < add(3,9):
    print("duck")
    x+=1 
print("goose")

add(3,9)

def initials(name):
    names = name.split(" ")
    initials = ""
    for name in names:
        initials += name[0]
    
    return initials

print(f"a = {ord("a")}")
print(f"97 = {chr(97)}")
