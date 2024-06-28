"""
0 a 5 niño pequeño
6 a 12 niños grandes
13 a 17 adolecentes
18 a 64 adultos
65 a 100 adulto mayor
"""
age = int(input("Enter your age: "))
gender = input("Enter your gender (male/female): ").lower()

if age < 0 or age > 100:
    print("Please enter a valid age")
else:
    if age < 6:
        if gender == "male":
            print("You are a little boy")
        elif gender == "female":
            print("You are a little girl")
    elif age < 12:
        if gender == "male":
            print("You are a big boy")
        elif gender == "female":
            print("You are a big girl")
    elif age < 18:
        if gender == "male":
            print("You are a teenager (man)")
        elif gender == "female":
            print("You are a teenager (woman)")
    elif age < 65:
        if gender == "male":
            print("You are an adult man")
        elif gender == "female":
            print("You are an adult woman")
    elif age <= 100:
        if gender == "male":
            print("You are an elderly man")
        else:
            print("You are an elderly woman")

