def palabras_con_letra_a(lista_palabras):
    resultados = {}
    
    for palabra in lista_palabras:
        letras = set(palabra)
        for letra in letras:
            if letra == 'a':
                if letra in resultados:
                    resultados[letra].append(palabra)
                else:
                    resultados[letra] = [palabra]
    
    return resultados




