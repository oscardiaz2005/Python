def dictionary(list):
    dictionary={}
    for word in list:
        dictionary[word]=0

    for word in list:
        for caracter in word:
            if caracter in word:
                dictionary[word] += 1
            else:
                dictionary[word] = 1   
    
    return dictionary    

