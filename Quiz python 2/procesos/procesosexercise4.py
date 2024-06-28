def palabras_con_letras_repetidas(lista_palabras):
    resultados = {}
    for palabra in lista_palabras:
        letras_repetidas = []
        letras_contadas = {}  
        for letra in palabra:
            if letra in letras_contadas:
                letras_contadas[letra] += 1
            else:
                letras_contadas[letra] = 1
        
        for letra, cantidad in letras_contadas.items():
            if cantidad > 1:
                letras_repetidas.append(letra)
        
        for letra in letras_repetidas:
            if letra in resultados:
                resultados[letra].append(palabra)
            else:
                resultados[letra] = [palabra]
    
    return resultados

