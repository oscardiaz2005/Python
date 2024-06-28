"""
Elabore un algoritmo que calcule e imprima las tablas de multiplicar desde uno hasta un numero dado por el 
usuario, el multiplicador desde uno hasta un numero dado por el usuario
"""
#while loop
print("While loop\n")

end_tables = int(input("Please enter the number of the table where you want to end the program: "))
end = int(input("Please enter the number where you want to end the multiplication tables: "))

table = 1
while table <= end_tables:
    print(f'\nTable number = {table}')
    begin = 1
    while begin <= end:
        result = table * begin
        print(f'{begin} * {table} = {result}')
        begin += 1
    table += 1

#for
print("\nFor loop\n")

table_limit = int(input("Enter the number of tables you want to print: "))
multiplication_limit = int(input("Enter the number up to which you want to print multiplication tables: "))

for i in range(1, table_limit + 1):
    print(f"\nTable number = {i}")
    for j in range(1, multiplication_limit + 1):
        print(f"{i} * {j} = {i * j}")
