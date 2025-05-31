#Contar cuántas veces aparece la letra "a" en cada frase de la lista.
frases = ["Hola", "Me gusta Python", "Estoy aprendiendo", "¡Genial!"]
letra_a = "a" #variable para guardar la letra que vamos a contar
total_a = 0
for frase in frases:
    total_a += frase.count(letra_a)
print("En la frase la letra a aparece:",total_a, "veces")
