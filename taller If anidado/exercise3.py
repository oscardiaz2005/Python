"""En un juego de preguntas a las que se responde Si o No gana quien responda correctamente las tres preguntas.
Si se responde mal a cualquiera de ellas ya no se pregunta la siguiente y termina el juego. Las preguntas son:
 ¿Colon descubrió América?
 ¿La independencia de México fue en el año 1810?
 ¿The Doors fue un grupo de rock Americano?
"""
game = True

while game:
    answer_one = input("Did Columbus discover America?  yes/not \n").lower()

    while answer_one != "not" and answer_one != "yes": 
        print("invalid answer")
        answer_one = input("Did Columbus discover America?  yes/not \n").lower()

    if answer_one == "not":
        print("the game has finished")
        print("you lost")
        break

    elif answer_one == "yes":

        answer_two = input("Was Mexico's independence in 1810? yes/not \n").lower()
        while answer_two != "not" and answer_two != "yes": 
            print("invalid answer")
            answer_two = input("Was Mexico's independence in 1810? yes/not \n").lower()

        if answer_two == "not":
            print("the game has finished")
            print("you lost")
            break
        elif answer_two == "yes":
            answer_three = input("Was The Doors an American rock group? yes/not \n").lower()
            while answer_three != "not" and answer_three != "yes":  
                print("invalid answer")
                answer_three = input("Was The Doors an American rock group? yes/not \n").lower()

            if answer_three == "not":
                print("the game has finished")
                print("you lost")
                break
            elif answer_three == "yes":
                print("you won")
                break





 


        


