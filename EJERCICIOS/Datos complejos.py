#creando una lista que se puede modificar
lista=["Juan","Programación",1.70,3]
#reemplazando valores
lista[3]=9
print(lista[3])
print(lista)


#creando una lista que no se puede modificar
tupla=("Juan","Programación",1.70,3)
print(tupla)


#creando un conjunto (set)
conjunto={"Juan","Programación",1.70,3}
print(conjunto)


#creando un diccionario, la estructura es ("clave":valor)
diccionario={
    "name":"Juan David",
    "age":20,
    "amigo1":"Axel",
    "amigo2":"Ariana",
    "amigo3":"Jandry"
}
print(diccionario["name"])
print(diccionario["amigo1"])
print(diccionario["age"]+12)


#operadores aritmeticos