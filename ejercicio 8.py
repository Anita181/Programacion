# Recibe una cadena de texto y devuelva cuántas vocales (a, e, i, o, u) tiene.
def contar_vocales(texto):
    contador = 0  # Empezamos en 0
    for letra in texto:  # Recorremos cada letra del texto
        if letra in "aeiouAEIOU":  # Si la letra es una vocal
            contador += 1  # Sumamos 1 al contador
    return contador  # Devolvemos el total de vocales al final.


print(contar_vocales("Hola Mundo")) # La función recibe "Hola Mundo" y cuenta las vocales.
