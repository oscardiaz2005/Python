race=input("which is the race of the dog ?  pitbull /buly /rottwhiller /labrador retriever /golden retriever /doberman /dogo argentino \n").lower()
if race == "pitbull":
    base_valor = 6000000
elif race == "buly":
    base_valor = 6500000
elif race == "rottwhiller":
    base_valor = 4000000
elif race == "labrador retriever":
    base_valor = 3500000
elif race == "golden retriever":
    base_valor = 3500000
elif race == "doberman":
    base_valor = 5000000
elif race == "dogo argentino":
    base_valor = 5500000      
else:
    print("Invalid race entered.")
    exit()

position=input("which was the position ? one /second /third \n").lower()
if position=="one":
    new_valor=base_valor*2
elif position=="second" :
    new_valor=base_valor+800000
elif position== "third":
    new_valor=base_valor+200000
else :
     print("Invalid position entered.")
     exit()

print(f'the dogs race is {race} so its valor is {base_valor}')
print(f'it got the position number {position} ')
print(f'the dogs new valor is {new_valor}')


