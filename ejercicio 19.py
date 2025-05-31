#Ver si una palabra contiene todas las vocales
palabra = input("Escribe una palabra: ")
vocales = ['a', 'e', 'i', 'o', 'u'] #lista de vocales
palabra = palabra.lower() #convertir todoas las letras en minusculas
tiene_todas = True  # asumimos que sí las tiene
for vocal in vocales:
    if vocal not in palabra:
        tiene_todas = False  # si falta una, ya no las tiene todas
        print(f"Falta la vocal: {vocal}")
if tiene_todas:
    print("¡Tiene todas las vocales!")
else:
    print("No tiene todas las vocales.")
