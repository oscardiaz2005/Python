
data_user={}
amount=int(input("how many data you want to add? "))

for i in range(amount):
    key=input(f'enter the key for the data number {i+1} ' )
    value=input("enter the value ")
    if key in data_user:
        print(f'the key {key} is already in the diccionary')
        newkey=input(f'enter the new key for the data number {i+1} ' )
        value=input("enter the value ")
        while newkey==key:
            print("invalid key , enter again")
            newkey=input(f'enter the new key for the data number {i+1} ' )
            value=input("enter the value ")
            data_user[newkey]=value
    else:    
        data_user[key]=value

print(data_user)


