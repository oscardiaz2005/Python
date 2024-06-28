menu=True
users=[]

while menu:
    print("\n1. Insert a new user")
    print("2. consult the list")
    print("3. looking for user in the list")
    print("4. modify user in the list")
    print("5. delete user in the list")
    print("6. exit")
    option=int(input("choose an option \n"))
    while option<1 or option>6:
        print("invalid option, please choose a correct option")
        option=int(input("choose an option \n"))
    
    if option==1 :
        amount=int(input("how many users do you want to insert? "))
        for i in range(amount):
          new_user=input("please enter the new user ")
          users.append(new_user)
          
    elif option==2 :
        print(users)   

    elif option ==3 :
        search_user=input("please enter the searched user ")
        if search_user in users:
            print("user found")
        else :
            print("the user has not been found")  

    elif option==4 :
        modify_user=input("which is the user that you want to modify ")
        if modify_user in users:
            inx=users.index(modify_user)
            change_user=input("plese enter the new valor for the user ")
            users[inx]=change_user
            print(" the user has been midified")
        else :
            print("the user has not been found")     

    elif option == 5:
        delete_user=input("which is the user that you want to delte ")
        if delete_user in users:
            users.remove(delete_user)
            print(" the user has been deleted")
        else:
            print("the user has not been found")   

    elif option==6:
        break

print("see you later")               



    
