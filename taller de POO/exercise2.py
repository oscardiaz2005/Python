from clases.clase_exercise2  import *
balance=int(input("enter your initial balance "))

print("\nWELCOME\n")
Acoount=BankAccount(balance)

while True:
    option=int(input("\nchoose an option \n1.Withdraw \n2.Add \n3.exit\n"))
    if option==1:
        money=int(input("Enter the amount you want to withdraw "))
        print(Acoount.withdraw(money))
    elif option==2:
        money=int(input("Enter the amount you want to add "))
        print(Acoount.add(money))
    elif option==3:
        break
    else:
        print("invalid option")    

print("SEE YOU :)")
