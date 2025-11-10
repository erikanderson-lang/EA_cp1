#EACP1

#What are dictionaries?
#they save info in keys and numbers

#How do dictionaries simply variables in a project?
#because we can have the same name for something but they are in different dictionaries

#What are key and value pairs?
#the things

#How do you build a dictionary?
# name = {"something":"thingamajig",
#
# }

#How do you call a value from a dictionary?
#print(f"name is {person["name"]}")

#How do you get each of the keys from a dictionary?
#for key in person.keys():

#How do you update a value in a dictionary?
#person["age"] -=1

#Can you add new key and value pairs to a dictionary during runtime?
#yes TRON


person = {
    "name":"jimbo",
    "age": 22,
    "job": "maverik",
    "sibiling": ["john", "johny", "johnathan"]
}
print(f"name is {person["name"]}")
print (person.keys())
for key in person.keys():
    if key == "sibiling":
        for name in key:
            print(f"{person['name']} has a sibiling named {name}")
    print(f"{key} is {person[key]}")

print(f"name is {person["name"]}")
print (person.keys())
for key in person.keys():
    if key == "sibiling":
        for name in [key]:
            print(f"{person['name']} has a sibiling named {name}")
    print(f"{key} is {person[key]}")