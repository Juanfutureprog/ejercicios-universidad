from datetime import date
# ejercicio 1
def saludo():
    nombre= input("Ingrese su nombre:")
    if nombre == "":
        print("No se puede ingresar un nombre vacio.")
    elif not nombre.replace(" ", "").isalpha():
        print("El nombre solo acepta letras")
    else:
        print(f"¡Hola {nombre}, bienvenido a nuestro programa!.")
saludo()


# ejercic 2
def suma():
    print("Ingrese dos números para realizar la suma")
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    resultado = num1 + num2
    print(f"La suma de {num1} y {num2} es: {resultado}.")
suma()


# ejecicio 3
def doble_triple():
    numero= float(input("Ingrese un nùmero para mostrar su doble y su triple:"))
    doble= numero*2
    triple= numero*3
    print(f"El doble de {numero} es: {doble} y el triple es: {triple}.")
doble_triple()


# ejercicio 4
def area_rectangulo():
    largo= float(input("Ingrese el largo del rectangulo:"))
    ancho= float(input("Ingrese el ancho del rectangulo:"))
    area= largo*ancho
    print(f"El area del rectangulo es: {area}.")
area_rectangulo()


# ejercicio 5
def transformacion_grados():
    celsius= float(input("Ingrese la temperatura en grado celsius:"))
    fahrenheit= (celsius*9/5)+32
    print(f"La temperatura en fahrenheit es: {fahrenheit:.2f}.")
transformacion_grados()



# ejercicio 6
def verificar_edad():
    edad= int(input("Ingrese su edad:"))
    if edad < 0:
        print("La edad no puede ser negativa")
    elif edad >= 18:
        print("Es mayor de edad")
    else:
        print("Es menor de edad")
verificar_edad()



# ejercicio 7
def numero_mayor():
    num1= float(input("Ingrese el primer numero:"))
    num2= float(input("Ingrese el segundo numero:"))
    if num1 > num2:
        print(f"El numero mayor entre {num1} y {num2} es:{num1}.")
    elif num2 > num1:
        print(f"El numero mayor entre {num1} y {num2} es:{num2}.")
    else:
        print("Los numeros ingresados son iguales.")
numero_mayor()


# ejercicio 8
def promedio_notas():
    nota1= float(input("Ingrese la primera nota:"))
    nota2= float(input("Ingrese la segunda nota:"))
    nota3= float(input("Ingrese la tercera nota:"))
    promedio= (nota1+nota2+nota3)/3
    print(f"El promedio de la tres notas es: {promedio:.2f}")
promedio_notas()


# ejercicio 9
def par_impar():
    numero= int(input("Ingrese un numero:"))
    if numero % 2 == 0:
        print(f"El numero {numero} es par.")
    else :
        print(f"El numero {numero} es impar.")
par_impar()



# ejercicio 10
def verificar_numero():
    numero=  float(input("Ingrese un numero:"))
    if numero > 0:
        print(f"El numero {numero} es positivo.")
    elif numero < 0:
        print(f"El numero {numero} es negativo.")
    else:
        print(f"El numero es cero")
verificar_numero()



# ejercicio 11
def calcular_descuento():
    valor= float(input("Ingrese el monto de la compra:"))
    if valor < 100:
        print(f"Tiene un descuento del 0%, el valor a pagar es: {valor}")
    elif 100 <= valor <= 150  :
        valor_final= (valor-(valor*0.10))
        print(f"Tiene un descuento del 10%, el valor a pagar es: {valor_final:.2f}")
    else:
        valor_final= (valor-(valor*0.15))
        print(f"Tiene un descuento del 15%, el valor a pagar es: {valor_final:.2f}")
calcular_descuento()


# ejercicio 12
def validar_edad():
    edad= int(input("Ingrese su edad:"))
    if edad < 0:
        print("La edad que ha ingresado es negativa.")
    elif edad <= 12:
        print(f"La edad: {edad} pertenece a la categoria niño.")
    elif 13 <= edad <= 17:
        print(f"La edad: {edad} pertenece a la categoria joven")
    else:
        print(f"La edad: {edad} pertenece a la categoria adulto.")
validar_edad()

# ejercicio 13
def ingreso_de_datos():
    usuario_definido= "Messi"
    contraseña_definida= "Vers2005"
    usuario= input("Ingrese su usuario:")
    contraseña= input("Ingrese su contraseña:")
    if contraseña_definida == contraseña and usuario_definido == usuario:
        print("Su usuario y contraseña son correctos, bienvenido al sistema.")
    elif contraseña_definida == contraseña or usuario_definido == usuario:
        print("Verifique su usuario o contraseña.")
    else:
        print("Su usuario y contraseña son incorrectos.")
ingreso_de_datos()


def mostrar_menu():
    print("Bienvenido a nuestro menu de opciones:")
    print("1. Saludar")
    print("2. Mostrar la fecha")
    print("3. Frase motivacional")
    print("4. Salir")

def saludar_menu():
    nombre= input("Ingrese su nombre:")
    print(f"Hola que tal {nombre}, espero que te encuentres bien ")

def mostrar_fecha():
    hoy= date.today()
    print(f"Hola que tal, la fecha de hoy es: {hoy}")

def frase_motivacional():
    print("No cuentes los días, haz que los días cuenten (Muhammad Ali)")


# ejercico 14
def menu_secundario():
    while True:
        mostrar_menu()
        opcion= input("Elija una de las siguientes opciones:").strip()
        if opcion == "1":
            saludar_menu()
        elif opcion == "2":
            mostrar_fecha()
        elif opcion == "3":
            frase_motivacional()
        elif opcion == "4":
            print("Hasta luego")
            break
        else:
            print("Elija una opcion valida")
menu_secundario()


# ejercicio 15
def año_bisiesto():
    year= int(input("Ingrese un año:"))
    if year % 400 == 0:
        print(f'El año {year} es bisiesto.')
    elif year % 100 == 0:
        print(f'El año {year} no es bisiesto.')
    elif year % 4 == 0:
        print(f'El año {year} es bisiesto.')
    else:
        print(f'El año {year} no es bisiesto.')
año_bisiesto()

# ejercicio 16
def calcular_numeros():
    numero1= float(input('Ingrese el primer número:'))
    numero2= float(input('Ingrese el segundo número:'))
    numero3= float(input('Ingrese el tercer número:'))
    if numero1 > numero2 and numero1 > numero3:
        print(f'El numero {numero1} es el mayor.')
    elif numero2 > numero1 and numero2 > numero3:
        print(f'El numero {numero2} es el mayor.')
    elif numero3 > numero1 and numero3 > numero2:
        print(f'El numero {numero3} es el mayor.')
    else:
        print('Todos los numeros son iguales')
calcular_numeros()

# ejercicio 17
def rendimiento_estudiantes():
    nota= float(input('Ingrese una nota:'))
    if 9 <= nota <= 10:
        print(f'Nota:{nota} - A(Excelente)')
    elif 7 <= nota <=8:
        print(f'Nota:{nota} - B(Bueno)')
    elif 5 <= nota <= 6:
        print(f'Nota:{nota} - C(Regular)')
    elif 0 <= nota <= 4:
        print(f'Nota:{nota} - D(Reprobado)')
    else:
        print('La nota esta fuera del rango.')
rendimiento_estudiantes()


# ejercicio 18
def operador_ternario():
    edad= int(input("Ingrese su edad:"))
    mensaje= "Acceso permitido" if edad >= 18 else "Acceso denegado"
    print(mensaje)
operador_ternario()


# ejercicio 19
def numeros_for():
    for i in range(1,11):
        print(i)
numeros_for()


# ejercicio 20
def suma_acumulada():
    suma=0
    while True:
        numero= float(input('Ingrese numeros para presentar una suma acumulada'))
        if numero == 0:
            break
        suma+=numero
    print(f'La suma total es: {suma}')
suma_acumulada()

# ejercicio 21
def tabla_multiplicar():
    numero= int(input('Ingrese un numero, y se presentará su tabla de multiplicar hasta el 12:'))
    for i in range (1,13):
        print(f'{numero} x {i} = {numero*i}')
tabla_multiplicar()


# ejercicio 22
def arreglo_nunmero_positivos():
    arreglo=[]
    longitud= int(input('Ingrese cuantos número desea ingresar:'))
    for i in range(longitud):
        numero=float(input('Ingrese un número:'))
        arreglo.append(numero)

    numeros_positivos=0
    for numero in arreglo:
        if numero > 0:
            numeros_positivos+=1
    print(f'La cantidad de números positivos es: {numeros_positivos}')
    for numero in arreglo:
        if numero > 0:
            print(numero)
arreglo_nunmero_positivos()

#ejercicio 23
def adivinar_numero():
    intentos=5
    numero_definido= 33
    contador=0
    while contador < intentos:
        numero= int(input('Ingrese numeros para adivianar numero definido:'))
        if numero > numero_definido:
            print('Te pasaste, el numero es menor')
        elif numero < numero_definido:
            print('El numero es mayor, sigue intentando.')
        elif numero == numero_definido:
            print(f'Felicidades,adivinaste el numero era: {numero_definido} ')
            break
        contador+=1
    else:
        print(f'No adivinaste, el numero era: {numero_definido}')
adivinar_numero()


#ejercicio 24
def calcular_promedio(numeros):
    prom= sum(numeros) / len (numeros)
    return prom


def promedio():
    arreglo = []
    longitud= int(input('Ingrese la cantidad de nùmeros que desea promediar:'))
    for i in range(longitud):
        numeros= float(input('Ingrese los numeros a promediar:'))
        arreglo.append(numeros)
    resultado= calcular_promedio(arreglo)
    print(f'El promedio es: {resultado:.2f}')
promedio()


#ejercicio 25
def primo(numero):
    if numero < 2:
        return False
    for i in range(2,numero):
        if numero % i == 0:
            return False
    return True
def verificar_primo():
    numero = int(input("Ingrese un numero:"))
    if primo(numero):
        print(f"{numero} es primo")
    else:
        print(f"{numero} no es primo")

verificar_primo()
# ejercicio 26
def factorial(numero):
    if numero == 0 or numero == 1:
        return 1
    return numero * factorial(numero - 1)

def numero_factorial():
    numero= int(input('Ingrese un nùmero:'))
    print(f'El resultado es {factorial(numero)}')
numero_factorial()


#ejercicio 27
def sumar():
    print("Ingrese dos números para realizar la suma")
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    resultado = num1 + num2
    print(f"La suma de {num1} y {num2} es: {resultado}.")


def restar():
    print("Ingrese dos números para realizar la resta")
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    resultado = num1 - num2
    print(f"La resta de {num1} y {num2} es: {resultado}.")


def multiplicar():
    print("Ingrese dos números para realizar la multiplicacion")
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    resultado = num1 * num2
    print(f"La multiplicacion de {num1} y {num2} es: {resultado}.")


def dividir():
    print("Ingrese dos números para realizar la division")
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    if num2 !=0:
        resultado = num1 / num2
        print(f"La division de {num1} y {num2} es: {resultado:.2f}.")
    else:
        print("No se puede dividir por cero")
def menu_calculadora():
    while True:
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")
        opcion = input("Elija una opcion:").strip()
        if opcion == "1":
            sumar()
        elif opcion == "2":
            restar()
        elif opcion == "3":
            multiplicar()
        elif opcion == "4":
            dividir()
        elif opcion == "5":
            print("Hasta luego")
            break
        else:
            print("Opcion invalida")


menu_calculadora()







































