from loginclass import Login
from procesos import verify

main_user=Login("oscar123","1234")

print("LOGIN\n")
acountant=0
while acountant<3 :
    user=input("USER\n")
    password=input("\nPASSWORD\n")

    new_user=Login(user,password)

    login=verify(main_user,new_user)
    if login:
        print(f"WELCOME {main_user.getuser()}")
        break
    else :
        acountant+=1
        print("user or password incorrect")
        if acountant>=3:
            print("Too many failed attempts, your acoount has been blocked")



