#EA cp1 
import time
#ask for password
password = (input("какой y тебя пароль, товарищ?: "))
#checking password for length
while True:
    if len(password) >=8:
        print("+1 point")
    else: print("-1point")
#checking password for capitals
    for num in password:
        print("+1 point")
    else: print("-1point")
#checking password for lowercase