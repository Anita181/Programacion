#Pide al usuario nombre y su edad, Si tiene menos de 13 → Imprime: "Hola [nombre], eres un niño/a".Si tiene entre 13 y 17 → Imprime: "Hola [nombre], eres un adolescente".Si tiene 18 o más → Imprime: "Hola [nombre], eres un adulto".
nombre = input("¿Cual es tu nombre? ")
edad = int(input("¿Cuántos años tienes? "))
if edad <= 13:
    print("Hola", nombre, "eres un niño/a")
elif edad >= 13 and edad <= 17:
    print("Hola", nombre, "eres un adolescente")
else:
    print("Hola", nombre, "eres un adulto")

#Pide una nota del 1 al 10 y di:10: ¡Excelente!7 a 9: ¡Muy bien!5 a 6: Pasaste.Menos de 5: Reprobaste.
nota = int(input("¿Dime tu nota? "))
if nota == 10:
    print("Excelente")
elif nota >= 7 and nota <= 9:
    print("Muy Bien")
elif nota >= 5 and nota <= 6:
    print("Pasaste")
elif nota < 5:
    print("Reprobaste")