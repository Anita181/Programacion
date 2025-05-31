saludo = "25" #variable global


def saludar():
    global saludo
    saludo = "Hola Mundo"


def saludaChanchito():
    saludo = 24  
    print(saludo)  


saludar()
resultado2 = saludo + 3
print(resultado2)
