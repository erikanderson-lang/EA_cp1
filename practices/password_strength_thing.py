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
if password == (f"{password}"):
        password.find("A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z")
        print("+1b")
else:
    print("You need a uppercase letter")
    #checking password for a number
if password == (f"{password}"):
        password.find("1,2,3,4,5,6,7,8,9,0")
        print("+1c")
else:
    print("You need a number")

    #checking password for lowercase
if password == (f"{password}"):
        password.find("a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z")
        print("+1d")
else:
    print("you need a lowercase letter" )

#checking for a special charicter
if password == (f"{password}"):
        password.find("!,@,#,$,%,^,&,*<(,),<,>,.,?,/,{,},|,-,_,+,=,`,~")
        print("+1e")
else:
    print("you need a special charecter" )
