#Bucles: Haz esto una y otra vez por cada cosa en una lista o texto
frutas = ["banana", "patilla", "mango"]
for fruta in frutas:
    print(fruta)
#palabra = input("Escribe una palabra: ")
#for letra in palabra:
    #print(letra)
palabra = input("Escribe una palabra: ")
palabra = palabra.lower()  # ahora todo es minúscula
contar_vocales = 0
for vocal in palabra:
    if vocal in "aeiou":
        contar_vocales += 1 #suma 
print("La palabra tiene", contar_vocales, "vocales")
