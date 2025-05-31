#Bucles while – Repetir hasta que tú digas basta Mientras esto sea verdadero... sigue haciendo esto.
contador = 1
while contador <= 5:
    print(contador)
    contador += 1  # suma 1 en cada vuelta
texto = input("Escribe algo: ")
while texto != "basta":
    texto = input("Escribe otra cosa (o 'basta' para salir): ")
print("Fin del programa")
intento = int(input("Adivina el número: "))
secreto = 7
while intento != secreto:
    intento = int(input("Intenta otra vez: "))
print("¡Adivinaste!")

