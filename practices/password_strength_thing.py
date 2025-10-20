#EA cp1 
import time
#ask for password
password = (input("какой y тебя пароль, товарищ?: "))
#checking password for length

if len(password) >=8:
        print("+1 point")
else: 
        print("you need eight characters at least")
time.sleep(1)

    #checking password for capitals

    #checking password for a number
if password == password.isalpha():
      print("placeholder")
else:
    print("You need a number")

    #checking password for lowercase
if password == (f"{password}"):
        password.find("a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z")
else:
    print("you need a lowercase letter" )
