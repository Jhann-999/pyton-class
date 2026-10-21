def mediana(vector):
    print(f"Vector original: {vector}")
    # sort != soted
    vector_ordenado = sorted(vector)
    print(f"Vector ordenado: {vector_ordenado}")
    n = len(vector_ordenado)
    if n % 2 == 1:    #IMPAR
        mediana = vector_ordenado[n//2]
        print(f"IMPAR n={n}, Mediana está en el indice {n//2}")
    else:             #PAR
        medio_1 = vector_ordenado[n//2]
        medio_2 = vector_ordenado[n//2-1]
        mediana = (medio_1 + medio_2) /2
        print(f"PAR n={n}, Mediana es el promedio de {medio_1} y {medio_2}")
    print(f"Mediana calculada: {mediana}")
    return mediana

vector_original = [7,1,5,3]
print(mediana(vector_original))