from procesos import *

while True:
    print("\n---- MAIN MENU ----\n")
    print("OPTIONS")
    print("1. add data")
    print("2. find a data")
    print("3. edit a data")
    print("4. delete a data")
    print("5. show data")
    print("6. exit")
    option = int(input("choose an option: "))

    if option == 1:      
        data_user = add_key()
        data_user = add_value(data_user)

    elif option == 2:
        searched_data = input("enter the data you want to find: ")
        result = find(searched_data, data_user)
        print(result)
    elif option == 3:
        searched_value = input("enter the value you want to edit: ")
        key = find_key_by_value(searched_value, data_user)
        if key:
            newvalue = input("enter the new value: ")
            data_user = edit(key, newvalue, data_user)
            print("the value was edited successfully")
        else:
            print("the value is not in the dictionary")    

    elif option == 4:
        searched_value = input("enter the value you want to delete: ")
        key = find_key_by_value(searched_value, data_user)
        if key:
            data_user = delete(key, data_user)
            print("the value was deleted successfully")
        else:
            print("the value is not in the dictionary")            
    elif option == 5:
        print(data_user)
    elif option == 6:
        break
    else:
        print("invalid option")
        
print("SEE YOU LATER ")



