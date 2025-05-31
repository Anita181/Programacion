#Calculadora de edad de mascotas
def edad_mascota(nombre, edad, tipo): #Esto crea una función que recibe un nombre, una edad y un tipo de animal (perro o gato).
    if tipo == "perro": #Si el animal es un perro, su edad se multiplica por 7.
        edad_final = edad * 7 
        tipo_edad = "años perrunos"
    elif tipo == "gato": #Si es un gato, se multiplica por 6.
        edad_final = edad * 6
        tipo_edad = "años gatunos"
    else: # Si no es ni perro ni gato, solo deja la edad tal cual.
        edad_final = edad
        tipo_edad = "años normales"
    print(nombre, "tiene", edad_final, tipo_edad)


edad_mascota("Firulais", 5, "perro") #llarmar la funcion
