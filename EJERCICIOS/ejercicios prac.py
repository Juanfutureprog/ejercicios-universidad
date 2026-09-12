# nums=[10,20,30,40,50]
# nums.append(60)
# nums.remove(20)
# print(nums)
#
# frutas= ["manzana", "pera", "uva", "mango"]
# for elemento in frutas:
#     print(elemento.upper())
#
# edad = int(input('Ingrese su edad: '))
#
# if edad >= 18:
#     dinero = input('Tiene dinero? (si/no): ')
#     if dinero == "si":
#         print("Puede entrar y comprar")
#     else:
#         print("Puede entrar pero no comprar")
# else:
#     print("No puede entrar")
#
# numeros = [5, 3, 8, 3, 1, 5, 9, 1]
# sin_repetidos = set(numeros)
# print(sin_repetidos)
# numeros_tupla = tuple(sin_repetidos)
# print(numeros_tupla)
#
# name= input('Ingese su nombre:')
# age= int(input('Ingese su edad:'))
# if age > 15:
#     menbresia= input('Tiene menbresia? (si/no)')
#     if menbresia == "si":
#         print(f'Bienvenido {name} tiene acceso completo')
#     else:
#         print(f'Bienvenido {name} tiene acceso limitado')
# else:
#     print(f'Lo sentimos {name} no puedes entrar')
#
# lista_vacia = []
#
# while True:
#     names = input('Ingrese un nombre (o "fin" para terminar): ')
#     if names == "":
#         print('No se pueden agregar nombres vacíos a la lista')
#     elif names == "fin":
#         break
#     elif names in lista_vacia:
#         print('El nombre ya existe en la lista')
#     else:
#         lista_vacia.append(names)
#         print(f'Se ha agregado {names} a la lista')
#
# print(lista_vacia)
#
# colores = ["rojo", "azul", "verde"]
# colores.append("amarillo")
# colores.insert(1, "negro")
# print(len(colores))
# print(colores)
#
# for i in range(1,11):
#     print(i)
#
# for i in range(2,21,2):
#     print(i)
#
#
# notas = [85, 42, 96, 61, 73, 55, 88]
# notas.sort()
# for i in notas:
#     if i >= 70:
#         print(f'{i} - Aprobado')
#     else:
#         print(f'{i} - Reprobado')
#
# numbers = []
# while True:
#     num = input('Ingrese un numero: ').lower()
#     if num == "fin":
#         print('Adios')
#         break
#     elif num == "":
#         print('No se pueden ingresar números vacíos')
#     else:
#         num = int(num)
#         if num in numbers:
#             print('El número ya existe en la lista')
#         else:
#             numbers.append(num)
#             print(f'Se ha agregado {num} a la lista')
#
# numbers.sort()
# print(numbers)
# for i in numbers:
#     if i % 2 == 0:
#         print(f'{i} - Es par')
#     else:
#         print(f'{i} - Es impar')
#
# carrito=[]
# while True:
#     print('1. Agregar producto')
#     print('2. Ver carrito')
#     print('3. Eliminar producto')
#     print('4. Salir')
#     opcion= input('Escoja una opcion:').lower().strip()
#     if opcion == "":
#         print('Ingrese una opcion valida')
#     elif opcion == "4":
#         print('Hasta luego')
#         break
#     else:
#         if opcion == "1":
#             producto= input('Ingese el nombre del prducto:').lower().strip()
#             carrito.append(producto)
#             print(f'Se ha agregqdo {producto.upper()} al carrito')
#         elif opcion == "2":
#             print('Productos disponibles en el carrito:')
#             for i in carrito:
#                 print(f'-{i}')
#         elif opcion == "3":
#             producto= input('Ingrese el nombre del producto a eliminar:').lower().strip()
#             if producto not in carrito:
#                 print('El producto no existe en el carrito')
#             else :
#                 carrito.remove(producto)
#                 print(f'Se ha eliminado {producto} del carrito')
#         else:
#             print('Ingrese una opcion valida')
#
#
# animals = ["perro", "gato", "loro", "gato", "perro", "pez", "gato"]
#
# for i, animal in enumerate(animals):
#     print(f'{i} - {animal}')
#
# print(f'El gato aparece {animals.count("gato")} veces')
# print(f'El pez está en la posición {animals.index("pez")}')
#
# alumno = {
#     'nombre':'Juan',
#     'edad': 20,
#     'nota': 80
# }
# for clave,valor in alumno.items():
#     print(f'{clave}: {valor}')
# alumno['nota']= 90
# alumno['ciudad']= 'Naranjito'
# del alumno['edad']
# print(alumno)
#
# alumnos= [
#     {'alumno' : 'Juan' , 'nota' : 80},
#     {'alumno' : 'Axel' , 'nota' : 90},
#     {'alumno' : 'Ariana' , 'nota' : 70}
# ]
# for alumno in alumnos:
#     if alumno['nota'] >= 70:
#         print(f'{alumno['alumno']} - {alumno["nota"]}: Aprobado')
#     else:
#         print(f'{alumno["alumno"]} - {alumno["nota"]}: Reprobado')
#
# print(f'Hay {len(alumnos)} alumnos en total')
#
# a = [
#     {"nombre": "Juan", "edad": 20},
#     {"nombre": "Maria", "edad": 25},
#     {"nombre": "Pedro", "edad": 30}
# ]
#
# b = [
#     {"nombre": "Maria", "edad": 25},
#     {"nombre": "Ana", "edad": 22},
#     {"nombre": "Juan", "edad": 20}
# ]
# lista_nueva= a + b
# resultado=[]
# for i in lista_nueva:
#     if i not in resultado:
#         i['fecha'] = 2026
#         resultado.append(i)
#
# print(resultado)
#
# productos = [
#     {"nombre": "manzana", "precio": 0.50, "stock": 10},
#     {"nombre": "leche", "precio": 1.20, "stock": 0},
#     {"nombre": "pan", "precio": 0.75, "stock": 5},
#     {"nombre": "jugo", "precio": 2.00, "stock": 0},
#     {"nombre": "arroz", "precio": 1.50, "stock": 8}
# ]
# productos_disponibles=[]
# for i in productos:
#     if i['stock'] > 0:
#         #cuando se esta dentro de un f string las claves de
#         #los dccionarios se deben poner con doble comilla
#         #una sola comilla causa conflictos
#         productos_disponibles.append(i)
#         print(f'{i["nombre"]} - Disponible - ${i["precio"]}')
#     else:
#         print(f'{i["nombre"]} - Agotado')
#
# print(f'Total de productos disponibles: {len(productos_disponibles)}')
#
# estudiantes = []
#
# while True:
#     nombre = input('Ingrese el nombre: ').lower().strip()
#     if nombre == "fin":
#         print('Adiós')
#         break
#     nota = float(input('Ingrese la nota: '))
#
#     diccionario = {}
#
#     if nota >= 70:
#         diccionario['nombre'] = nombre
#         diccionario['nota'] = nota
#         diccionario['estado'] = 'Aprobado'
#     else:
#         diccionario['nombre'] = nombre
#         diccionario['nota'] = nota
#         diccionario['estado'] = 'Reprobado'
#
#     estudiantes.append(diccionario)
#
# for i in estudiantes:
#     print(f'Nombre: {i["nombre"]}, Nota: {i["nota"]}, Estado: {i["estado"]}')
# Usa print() cuando quieras ver qué está pasando o mostrarle un resultado al usuario.
# Usa return cuando quieras que una función calcule algo y te devuelva ese valor
# para seguir trabajando con él en tu código.
#
# def calcular_promedio(lista):
#     promedio = sum(lista) / len(lista)
#     return promedio
#
# notas = [80, 90, 70, 85, 95]
# resultado = calcular_promedio(notas)
# print(f'El promedio de las notas es: {resultado}')
#
# def verificar_aprobados(nombre,nota):
#     if nota >= 70:
#         return f'{nombre} - Aprobado'
#     else:
#         return f'{nombre} - Reprobado'
#
# estudiantes= [{'nombre':'Juan', 'nota': 100}, {'nombre':'Maria', 'nota': 60}]
# for i in estudiantes:
#     print(verificar_aprobados(i["nombre"], i["nota"]))
#
# NUEVO TEMA: LIST COMPREHENSIONS
# ESTRUCTURA:
# nueva_lista = [expresion for elemento in lista]
# nueva_lista = [expresion for elemento in lista if condicion]
# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# nueva_lista= [numero * 2 for numero in numeros]
# print(nueva_lista)
# nueva_lista2= [numero for numero in numeros if numero % 2 == 0]
# print(nueva_lista2)
# nueva_lista3= [numero * 3 for numero in numeros if numero % 2 == 0]
# print(nueva_lista3)
# lista4= [numero * 4 for numero in range(1,101)]
# print(lista4)
#
#
# estudiantes = [
#     {"nombre": "Juan", "nota": 85},
#     {"nombre": "Maria", "nota": 60},
#     {"nombre": "Pedro", "nota": 72},
#     {"nombre": "Ana", "nota": 45},
#     {"nombre": "Luis", "nota": 90}
# ]
# aprobados= [aprobados for aprobados in estudiantes if aprobados["nota"] >= 70]
# reprobados= [reprobados["nombre"] for reprobados in estudiantes if reprobados["nota"] < 70]
# def resumen_estudiantes(aprobados,reprobados):
#     print(f'Estudiantes aprobados: {len(aprobados)}, Estudiantes reprobados: {len(reprobados)}')
# resumen_estudiantes(aprobados,reprobados)
#
# def doble_triple():
#     numero= input('Ingrese un numero para presentar su doble y su triple:')
#     if numero.isalpha():
#         print('Ingrese un numero')
#     else:
#         numero= int(numero)
#         doble= numero*2
#         triple= numero*3
#         print(f'El doble de {numero} es: {doble} y el triple es: {triple}')
# while True:
#     opcion= input('Ingrese 1 para ejecutar el programa o 2 para salir: ')
#     if opcion == '1':
#         doble_triple()
#     elif opcion == '2':
#         print('Hasta luego')
#         break
#     else:
#         print('Ingrese una opcion valida')
#
#
# def compras():
#     compras=[]
#     n_compras= int(input('Ingrese el numero de compras: '))
#     for i in range(n_compras):
#         compras.append(float(input('Ingrese el valor de la compra: ')))
#     valor_total= sum(compras) +(sum(compras) * 0.15)
#     print(f'El valor total de las compras es: ${valor_total}')
# while True:
#     opcion= input('Ingrese 1 para ejecutar el programa o 2 para salir: ')
#     if opcion == '1':
#         compras()
#     elif opcion == '2':
#         print('Hasta luego')
#         break
#     else:
#         print('Ingrese una opcion valida')

#CONCEPTO *args, que permite recibir cualquier cantidad de valores
# *args guarda todos los valores en una tupla automáticamente, por eso puedes recorrerla con un for:
# Python lo hace automáticamente porque una tupla es inmutable, es decir, los valores que entran a la función no se deben modificar,
# solo usarse. Además la tupla mantiene el orden en que los ingresaste.
# El nombre args es una convención, podrías llamarlo * numeros o * datos, lo importante es el * adelante
# def calcular_promedio(*notas):
#     return sum(notas)/len(notas)
# promedio=calcular_promedio(10,20,30,40,50)
# print(f'El promedio es: {promedio}')

#CONCEPTO **kwargs:recibe cualquier cantidad de clave: valor (como un diccionario)
# def registrar_persona(**datos):
#     resultado= ""
#     for clave, valor in datos.items():
#         resultado+= f'{clave} : {valor} \n' #el \n es para dar un salto de linea
#     return resultado
# print(registrar_persona(nombre="Juan", edad=20, ciudad="Guayaquil", carrera="Sistemas"))
# precios = [10.5, 20.0, 35.75, 8.25, 50.0]
# descuento= list(map(lambda x: x * 0.85, precios))
# print(descuento)
#
# edades = [15, 22, 17, 30, 14, 25, 18, 16, 21]
# mayores_edad= list(filter(lambda x: x >=18, edades))
# print(mayores_edad)
#
# productos = [
#     {"nombre": "manzana", "precio": 0.50},
#     {"nombre": "leche", "precio": 1.20},
#     {"nombre": "pan", "precio": 0.75},
#     {"nombre": "jugo", "precio": 2.00},
#     {"nombre": "arroz", "precio": 1.50}
# ]
# nuevos_productos= list(map(lambda x: {"nombre": x["nombre"], "precio": x["precio"] * 0.90},filter(lambda x: x["precio"]> 1.00, productos)))
# print(nuevos_productos)
def aplicar_operacion(lista, funcion):
    return [funcion(x) for x in lista]

numeros = [1, 2, 3, 4, 5]

# le pasamos una lambda como función
resultado = aplicar_operacion(numeros, lambda x: x * 2)
print(resultado)  # [2, 4, 6, 8, 10]