#EA_cp1 User signin
username = ("Erik Anderson")
password = ("vfvf")
nameinput = input("username: ").strip().lower().title()
passwordinput = input("Password: ").strip().lower()

if nameinput == username and passwordinput == password: 
    print(f"Correct, Welcome {username}.")
else:
     print("incorrect.")