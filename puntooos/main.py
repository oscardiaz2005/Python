"""
algoritmo pedir registrarse  con usuario y contraseña 
verificar si la contraseña tenga un * un . un ! y que la cantida de caracteres sea minimo 8 caracters
sino no se deja registrar
despues debe permitir hacer el logeo 
"""

def verify_password (password):
    asterisc=False
    interrogation=False
    dot=False
    accountant=0

    for i in password:
        accountant+=1
        if i ==".":
            dot=True 
        elif i=="*" :
            asterisc=True
        elif i =="?":
            interrogation=True  
             
    if asterisc and interrogation and dot and accountant>=8:
        return  password
    else:
        return "password invalid"
    
user=input("enter your user ")
password=input("enter your password ")

correct_password=verify_password(password)

if correct_password=="password invalid":
    print("invalid password")
else:
    print("you have been registered")   
    print("LOGIIIIN")
    correct_password2=correct_password 
    tries = 0
    tries_left = 3 
    while tries < 3:
        user_try = input("Please enter your user: ")
        password_try = input("Please enter your password: ")

        if user_try == user and password_try == correct_password2:
            print("Welcome back")
            break
        else:
            tries += 1
            tries_left -= 1
            print("Incorrect user or password.")
            print(f'You have {tries_left} attempt(s) left.')

        if tries == 3:
            print("Your account has been blocked.")

 




