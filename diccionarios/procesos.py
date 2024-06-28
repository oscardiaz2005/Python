def add_key():
    data_user = {}
    print("---- ADD KEYS ----")
    print("Please enter 5 unique keys")
    i = 0
    while len(data_user) < 5:
        key = input(f'Enter key number {i+1}: ')
        if key in data_user:
            print(f'The key {key} is already in the dictionary. Please enter a new key.')
        else:
            data_user[key] = ""
            i += 1
    return data_user



def add_value(data_user):
    print("----ADD VALUES---")
    for c in data_user:
        value=input(f'enter the value for the key {c} ')
        data_user[c]=value
    return data_user    


def find(key,dictionary):
    if key in dictionary:
        message= f'{key} == {dictionary[key]}'
    else:
        message="the data is not in the dictionary"
    return message     

def find_key_by_value(value, dictionary):
    for key, val in dictionary.items():
        if val == value:
            return key
    return None


def verify(key,dictionary,):
    if key in dictionary:
        return True
    else :
        return False
    
def edit(key,value,dictionary):
    dictionary[key]=value
    return dictionary

def delete(key,dictionary):
    del dictionary[key]
    return dictionary




