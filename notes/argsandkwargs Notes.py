#EACP1

#What are positional arguments?
#an arguement in a position

#What are keyword arguments?
#the peramiter of a call

#How do you set a default parameter value?
#the name of the varriable 

#How do alter a function to take in an unknown number of arguments?
#args and kwargs (kwarguments)

#def hello(age = 121,name = "Jimbo"):
#    return f"hello {name}"
#print(hello())

def hello(*names, last_name):
    print(type(names))
    for n in names:
        print(f"hello {n} {last_name}")

hello("E ","jimbo ", last_name="E")
def full (**names):
    if names['middle']:
        return 
    
 
