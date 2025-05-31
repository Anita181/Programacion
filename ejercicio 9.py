# Cuenta cuántas veces aparece una letra específica en una palabra o frase ingresada por el usuario.

def contar_letras(texto, letra): #pylint: disable=unused-argument
    contador = 0
    for caracter in texto:  # Iteramos sobre cada letra de la palabra
        if caracter == letra:  # Comparamos con la letra buscada
            contador += 1
    return contador  # Retornamos el resultado
palabra = input("Escribe una palabra o frase: ")  # pedimos entrada al usuario
buscar = input("Escoge una letra para contar: ")
resultado = contar_letras(palabra, buscar)
print(f'La letra "{buscar}" aparece {resultado} veces en la palabra')
