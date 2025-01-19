#quiero pedirle al usuario un numero y mostrar la tabla de multiplicar de ese numero con su resultado
numero = input("Dime un numero: ")
numero=int(numero)
for i in range(0,11):
    resultado = numero*i
    print(f"{numero} * {i} = {resultado}")

