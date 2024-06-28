user = "oscar2005"
password = "abc123"
tries = 0
tries_left = 3

while tries < 3:
    user_try = input("Please enter your user: ").lower()
    password_try = input("Please enter your password: ").lower()

    if user_try == user and password_try == password:
        print("Welcome!")
        break
    else:
        tries += 1
        tries_left -= 1
        print("Incorrect user or password.")
        print(f'You have {tries_left} attempt(s) left.')

if tries == 3:
    print("Your account has been blocked.")



