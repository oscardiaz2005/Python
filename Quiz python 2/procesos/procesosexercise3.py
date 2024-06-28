def young(dictionary) :
    ages=[13]
    names=[]
    for name , age in dictionary.items():
        names.append(name)
        ages.append(age)

    inx=ages.index(min(ages))
    return names[inx]

    
 

       


