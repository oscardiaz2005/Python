def splitString(string,chars):
    for caracter in string:
        chars.append(caracter)
    return chars


def counttimes(chars, dictionary):
    for char in chars:
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1
    return dictionary        


        
        


        
    
