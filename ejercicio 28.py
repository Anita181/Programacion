#La Súper Función de Análisis de Texto
def funcion(texto):
    vocales = 0 
    for vocal in texto: #recorre todas las vocales en el texto
        if vocal in "aeiou":
            vocales += 1 #suma 1
    palabras = texto.split() #divide el texto en palabras
    cantidad_palabras = len(palabras) #cuenta la cantidad de palabras
    palabra_mas_larga = max(palabras, key=len) #saca cual es la palabra mas larga
    print("El texto tiene:", vocales, "vocales")
    print("El texto tiene:", cantidad_palabras, "palabras")
    print("La palabra mas larga es:", palabra_mas_larga)
funcion("la vaca loca tiene cabeza y no tiene cola")
    