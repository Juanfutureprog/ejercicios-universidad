#primer ejercicio
#pedir datos y presentarlos
nombre= input("Ingrese su nombre:")
carrera= input("Ingrse su carrera: ")
edad= int(input("Ingrese su edad: "))
print(f"SU nombre es: {nombre}, su carrera es: {carrera} y tiene una edad de {edad} años.")


#segundo ejercicio
#pedir un numero, presentar su doble y su triple
numero= int(input("Ingrese un número:"))
doble= numero*2
triple= numero*3
print(f"El doble del númnero {numero} es: {doble} y el triple es: {triple}")


#tercer ejercicio
#pedir un numero y hacer operaaciones
number1=int(input("Ingrese un número: "))
number2=int(input("Ingrese un segundo númnero: "))
suma=number1+number2
resta=number1-number2
multiplicacion=number1*number2
division=number1/number2
print(f"El rsultado de la suma es: {suma}")
print(f"El rsultado de la resta es: {resta}")
print(f"El rsultado de la multiplicacion es: {multiplicacion}")
print(f"El rsultado de la division es: {division:.2f}")
