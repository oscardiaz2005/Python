current_level = 1
gold_coins = 0
silver_coins = 0
weapons_obtained = []

print("WELCOME TO HEROS ADVENTURE\n")
while current_level <= 5:
    print(f"Level {current_level}:")
    
    if current_level == 1:
        print("Exploring the Deep Jungle")
        print("You must answer at least 2 out of 5 questions correctly to advance.\n")
        correct_answers = 0 
        for _ in range(5):
            answer = input("Is 2 + 2 equal to four? (y/n) ").lower()
            while answer!="y" and answer!="n":
                print("invalid answer only y or n")
                answer = input("Is 2 + 2 equal to four? (y/n) ").lower()
            if answer == "y":
                correct_answers += 1
        if correct_answers >= 2:
            print("You passed level 1!")
            weapon_obtained = "tribal dagger"
            if weapon_obtained not in weapons_obtained:
                weapons_obtained.append(weapon_obtained)
            silver_coins += 20000 + correct_answers * 5000
        else:
            print("Sorry, you did not pass level 1. You are doomed to get lost in the jungle.")
            break
    
    elif current_level == 2:
        print("Crossing the River of Secrets")
        print("You must answer at least 3 out of 5 questions correctly to advance.\n")
        correct_answers = 0
        for _ in range(5):
            answer = input("Is 5 + 5 equal to ten? (y/n) ").lower()
            while answer!="y" and answer!="n":
                print("invalid answer only y or n")
                answer = input("Is 5 + 5 equal to ten? (y/n) ").lower()
            if answer == "y":
                correct_answers += 1
        if correct_answers >= 3:
            print("You passed level 2!")
            weapon_obtained = "Map of the Temples"
            if weapon_obtained not in weapons_obtained:
                weapons_obtained.append(weapon_obtained)            
            silver_coins += 30000 + correct_answers * 10000
        else:
            print("Sorry, you did not pass level 2.")
            pay_option = input("Do you want to pay 40,000 silver coins for a second chance? (y/n) ").lower()
            if pay_option == "y":
                if silver_coins >= 40000:
                    silver_coins -= 40000
                    print("You have paid 40,000 silver coins for a second chance.")
                    extra_correct_answers = 0
                    for _ in range(5):
                        answer = input("Is 5 + 5 equal to ten? (y/n) ").lower()
                        while answer!="y" and answer!="n":
                            print("invalid answer only y or n")
                            answer = input("Is 5 + 5 equal to ten? (y/n) ").lower()
                        if answer == "y":
                            extra_correct_answers += 1
                    if extra_correct_answers >= 3:
                        print("You passed level 2 with the second chance!")
                        silver_coins += 30000 + extra_correct_answers * 10000
                        weapon_obtained = "Map of the Temples"
                        if weapon_obtained not in weapons_obtained:
                            weapons_obtained.append(weapon_obtained)     

                    else:
                        print("Sorry, you did not pass level 2 even with the second chance. You are doomed to die.")
                        break
                else:
                    print("You do not have enough coins to pay for the second chance. You are doomed to die.")
                    break
            else:
                print("You are doomed to die.")
                break
    
    elif current_level == 3:
        print("In Search of the Ancient Amulet")
        print("You must answer five questions correctly to advance.\n")
        correct_answers = 0
        for _ in range(5):
            answer = input("Is 10 / 2 equal to five? (y/n) ").lower()
            if answer == "y":
                correct_answers += 1
        if correct_answers == 5:
            print("You passed level 3!")
            gold_coins += 100000 + correct_answers * 20000
            weapon_obtained = "Ancient Amulet"
            if weapon_obtained not in weapons_obtained:
                weapons_obtained.append(weapon_obtained)             


        elif correct_answers >= 3:
            return_option = input("You did not pass all the questions. Do you want to return to level 1 (60,000 silver coins) or level 2 (120,000 silver coins)? (1/2) ").lower()
            if return_option == "1":
                if silver_coins >= 60000:
                    silver_coins -= 60000
                    print("You returned to level 1.")
                    current_level = 0
                else:
                    print("You do not have enough coins to return to level 1. You are doomed to die.")
                    break
            elif return_option == "2":
                if silver_coins >= 120000:
                    silver_coins -= 120000
                    print("You returned to level 2.")
                    current_level = 1
                else:
                    print("You do not have enough coins to return to level 2. You are doomed to die.")
                    break
            else:
                print("You are doomed to die.")
                break
        else:
            print("You are doomed to die.")
            break
    
    elif current_level == 4:
        print("Challenging the Ancient Ruins")
        print("You must answer both questions correctly to advance.\n")
        correct_answers = 0
        for _ in range(2):
            answer = input("Is 3 * 3 equal to eight? (y/n) ").lower()
            if answer == "n":
                correct_answers += 1
        if correct_answers == 2:
            print("You passed level 4!")
            gold_coins += 1000000
            weapon_obtained = "Spear of Destiny"
            if weapon_obtained not in weapons_obtained:
                weapons_obtained.append(weapon_obtained)             
        elif correct_answers == 1:
            return_option = input("You did not answer both questions correctly. Do you want to return to level 1 (160,000 gold coins and 40,000 silver coins)? (y/n) ").lower()
            if return_option == "y":
                if gold_coins >= 160000 and silver_coins >= 40000:
                    gold_coins -= 160000
                    silver_coins -= 40000
                    print("You returned to level 1.")
                    current_level = 0
                else:
                    print("You do not have enough coins to return to level 1. You are doomed to die.")
                    break
            else:
                print("You are doomed to die.")
                break
        else:
            print("You are doomed to die.")
            break
    
    elif current_level == 5:
        print("Confrontation in the Sacred Temple")
        print("You must answer three final questions correctly to defeat the Lord of Shadows.\n")
        correct_answers = 0
        for _ in range(3):
            answer = input("Is 1 + 1 equal to two? (y/n) ").lower()
            if answer == "y":
                correct_answers += 1
        if correct_answers == 3:
            print("You passed level 5! You are the Master Explorer!")
        else:
            print("Sorry, you could not defeat the Lord of Shadows. Your fate is sealed.")
            break
    
    print(f"\nSummary up to level {current_level}:")
    print(f"Gold coins obtained: {gold_coins}")
    print(f"Silver coins obtained: {silver_coins}")
    print(f"Weapons obtained: {weapons_obtained}")
    print() 
    
    current_level += 1


print("\nThanks for playing the adventure!")









