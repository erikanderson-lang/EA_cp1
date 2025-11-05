#EA cp1 
import time
#ask for password
password = (input("Password: "))
#checking password for length

if len(password) >=8:
        print("+1a")
else: 
        print("you need eight characters at least")
time.sleep(1)

    #checking password for capitals
if any(ch.isupper() for ch in password):
    print("+1b")
else:
    print("You need a uppercase letter")
    #checking password for a number

if any(ch.isdigit() for ch in password):
    print("+1c")
else:
    print("you need one digit")

    #checking password for lowercase
if any(ch.islower() for ch in password):
    print("+1d")
else:
    print("you need a lowercase letter" )

#checking for a special charicter
sepschar = set("!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~")
if any(ch in sepschar for ch in password):
     print("+1e")
else:
    print("you need a special charecter" )

