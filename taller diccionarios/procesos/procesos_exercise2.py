def procesar_multa(distancia, velocidad_maxima, tiempo):
    if tiempo < 0:
        return "<ERROR>"
    
    distancia_km = distancia / 1000
    
    velocidad_media = (distancia_km / (tiempo / 3600))
    
    if velocidad_media <= velocidad_maxima:
        return "<OK>"
    elif velocidad_media <= velocidad_maxima * 1.2:
        return "<MULTA>"
    else:
        return "<CURSO SENSIBILIZACION>"