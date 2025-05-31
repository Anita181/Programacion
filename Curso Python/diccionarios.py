# DICCIONARIOS

my_dict = {"a", "b"}
print(type(my_dict))

my_dict = {"Nombre":"Anais", 
           "Apellido":"Gonzalez", 
           "Apodo":"Any"}
print(type(my_dict))

print(my_dict["Apodo"])

print(my_dict.keys())
print(my_dict.values())

my_dict = list(my_dict)
print(my_dict)