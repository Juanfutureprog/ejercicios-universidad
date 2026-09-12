# class Estudiante:
#
#     def __init__(self, nombre, edad, carrera, promedio):
#         self.nombre= nombre
#         self.edad= edad
#         self.carrera= carrera
#         self.promedio= promedio
#
#     def __str__(self):
#         return f'{self.nombre} - {self.edad} - {self.carrera} - {self.promedio}'
#
#     def aprobado(self):
#         if self.promedio >= 7:
#             print(f'{self.nombre} aprobado')
#         else:
#             print(f'{self.nombre} reprobado')
#
#     def actualizar_promedio(self, nuevo_promedio):
#         self.promedio= nuevo_promedio
#
# alumno1= Estudiante('Juan', 20, 'Ingenieria de software', 5)
# print(f'ESTADO ACTUAL DEL ESTUDIANTE: {alumno1}')
# alumno1.aprobado()
# alumno1.actualizar_promedio(6)
# print(f'ESTADO ACTUAL DEL ESTUDIANTE: {alumno1}')
# alumno1.aprobado()

# class CuentaBancaria:
#     def __init__(self, numero_cuenta, titular, saldo):
#         self.numero_cuenta= numero_cuenta
#         self.titular= titular
#         self.saldo= saldo
#
#     def depositar(self, dinero):
#         self.saldo += dinero
#         print(f'Depositaste ${dinero} en tu cuenta')
#
#     def retirar(self, dinero):
#         if dinero < self.saldo or dinero == self.saldo:
#             self.saldo -= dinero
#             print(f'Retiraste ${dinero} de tu cuenta')
#         else:
#             print('Saldo insuficiente')
#
#     def mostrar_estado(self):
#         print(f'Titular: {self.titular}, Saldo: ${self.saldo}, Numero de cuenta: {self.numero_cuenta}')
#
# cuenta1= CuentaBancaria(123456789, 'Juan', 1000)
# cuenta1.mostrar_estado()
# cuenta1.depositar(500)
# cuenta1.mostrar_estado()
# cuenta1.retirar(200)
# cuenta1.mostrar_estado()
#
# class Productos:
#     def __init__(self, codigo, nombre, precio, stock):
#         self.codigo= codigo
#         self.nombre= nombre
#         self.precio= precio
#         self.stock= stock
#
#     def comprar(self, cantidad):
#         if cantidad <= self.stock:
#             self.stock -= cantidad
#             print(f'Has comprado {cantidad} unidades de {self.nombre}')
#         else:
#             print('No hay stock suficiente')
#
#     def agregar_producto(self, cantidad):
#         self.stock += cantidad
#         print(f'Se agregaron {cantidad} unidades de {self.nombre}')
#
#     def calcular_total(self):
#         return f'Valor total: {self.precio * self.stock}'
#
# producto1= Productos(1, 'Coca_Cola', 100, 10)
# producto1.comprar(5)
# producto1.agregar_producto(5)
# print(producto1.calcular_total())


# class Empleado:
#     def __init__(self, nombre, salario):
#         self.nombre= nombre
#         self.salario= salario
#
#     def trabajar(self):
#         print(f' {self.nombre} está trabajando')
#
# class Programador(Empleado):
#     def trabajar(self):
#         super().trabajar()
#         print(f'{self.nombre} está programando')
#
# class Diseñador(Empleado):
#     def trabajar(self):
#         super().trabajar()
#         print(f'{self.nombre} esta creando diseños')
#
#
# persona1= Empleado('Ariana', 1000)
# persona2= Programador('Juan', 2000)
# persona3= Diseñador('Maria', 3000)
# persona1.trabajar()
# persona2.trabajar()
# persona3.trabajar()


# class Habitacion:
#
#     def __init__(self, numero, tipo, precio, disponibilidad):
#         self.numero = numero
#         self.tipo = tipo
#         self.precio = precio
#         self.disponibilidad = disponibilidad
#
#     def __str__(self):
#         return f'INFO HABITACION: Numero: {self.numero}, Precio: {self.precio}, Disponibilidad: {self.disponibilidad}'
#
#
# class Hotel:
#
#     def __init__(self, nombre):
#         self.nombre = nombre
#         self.habitaciones = []
#
#     def agregar_habitacion(self, habitacion):
#         self.habitaciones.append(habitacion)
#
#     def reservar(self, numero):
#         for habitacion in self.habitaciones:
#             if habitacion.numero == numero:
#                 if habitacion.disponibilidad == True:
#                     habitacion.disponibilidad = False
#                     print(f'Habitacion {numero} reservada exitosamente')
#                 else:
#                     print(f'La habitacion {numero} no está disponible')
#                 return
#         print(f'Habitacion {numero} no encontrada')
#
#     def liberar(self, numero):
#         for habitacion in self.habitaciones:
#             if habitacion.numero == numero:
#                 if habitacion.disponibilidad == False:
#                     habitacion.disponibilidad = True
#                     print(f'Habitacion {numero} liberada exitosamente')
#                 else:
#                     print(f'La habitacion {numero} ya estaba disponible')
#                 return
#         print(f'Habitacion {numero} no encontrada')
#
#     def habitaciones_disponibles(self):
#         for habitacion in self.habitaciones:
#             if habitacion.disponibilidad == True:
#                 print(habitacion)
#
#     def habitaciones_nodisponibles(self):
#         for habitacion in self.habitaciones:
#             if habitacion.disponibilidad == False:
#                 print(habitacion)
#
#
# habitacion1 = Habitacion(5, 'Familiar', 75, True)
# habitacion2 = Habitacion(6, 'Individual', 45, False)
# habitacion3 = Habitacion(7, 'Doble', 55, False)
# habitacion4 = Habitacion(8, 'Triple', 65, True)
# hotel = Hotel('ARIANA HOTELES')
# hotel.agregar_habitacion(habitacion1)
# hotel.agregar_habitacion(habitacion2)
# hotel.agregar_habitacion(habitacion3)
# hotel.agregar_habitacion(habitacion4)
# hotel.reservar(5)
# hotel.reservar(6)
# hotel.reservar(10)
# hotel.liberar(7)
# hotel.liberar(8)
# hotel.liberar(19)
# hotel.habitaciones_disponibles()
# hotel.habitaciones_nodisponibles()



# class Figura:
#     def calcular_perimetro(self):
#         print('No se puede calcular el area')
#
#     def calcular_area(self):
#         print('No se puede calcular el perimetro')
#
#
# class Rectangulo(Figura):
#     def __init__(self, largo, ancho):
#         self.largo = largo
#         self.ancho = ancho
#
#     def calcular_perimetro(self):
#         perimetro = 2 * self.largo + 2 * self.ancho
#         print(f'El perimetro del rectangulo es {perimetro}')
#
#     def calcular_area(self):
#         area = self.largo * self.ancho
#         print(f'El area del rectangulo es {area}')
#
#
# class Triangulo(Figura):
#     def __init__(self, ladoA, ladoB, ladoC, base, altura):
#         self.ladoA = ladoA
#         self.ladoB = ladoB
#         self.ladoC = ladoC
#         self.base = base
#         self.altura = altura
#
#     def calcular_perimetro(self):
#         perimetro = self.ladoA + self.ladoB + self.ladoC
#         print(f'El perimetro del triangulo es {perimetro}')
#
#     def calcular_area(self):
#         area = (self.base * self.altura) / 2
#         print(f'El area del triangulo es {area}')
#
#
# class Circulo(Figura):
#     def __init__(self, radio):
#         self.radio = radio
#
#     def calcular_perimetro(self):
#         perimetro = 2 * 3.14 * self.radio
#         print(f'El perimetro del circulo es {perimetro}')
#
#     def calcular_area(self):
#         area = 3.14 * (self.radio ** 2)
#         print(f'El area del circulo es {area}')
#
#
# figuras = [Rectangulo(20, 10), Triangulo(18, 20, 19, 30, 25), Circulo(8)]
# for figura in figuras:
#     figura.calcular_perimetro()
# for figura in figuras:
#     figura.calcular_area()

# class Animal:
#     def hacer_sonido(self):
#         print('El animal hace un sonido')
#
#
# class Perro:
#     def __init__(self, nombre):
#         self.nombre = nombre
#
#     def hacer_sonido(self):
#         print(f'El perro {self.nombre} dice guau')
#
#
# class Gato:
#     def __init__(self, nombre):
#         self.nombre = nombre
#
#     def hacer_sonido(self):
#         print(f'El gato {self.nombre} dice miau')
#
#
# class Ave:
#     def __init__(self, nombre):
#         self.nombre = nombre
#
#     def hacer_sonido(self):
#         print(f'El ave {self.nombre} canta')
#
#
# animales = [Perro('Luna'), Gato('Mufasa'), Ave('Piolin')]
#
# for animal in animales:
#     animal.hacer_sonido()

class Cliente:
    def __init__(self, nombre, cedula, celular):
        self.nombre = nombre
        self.cedula = cedula
        self.celular = celular

    def mostrar_informacion(self):
        print(f'Datos del cliente: Nombre: {self.nombre}, Cedula: {self.cedula}, Celular: {self.celular}')


class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar_informacion(self):
        print(f'Datos del producto: Nombre: {self.nombre}, Precio: {self.precio}')


class Pedido:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def eliminar_producto(self, nombre):
        for producto in self.productos:
            if producto.nombre == nombre:
                self.productos.remove(producto)
                print(f'{nombre} eliminado del pedido')
            return
        print(f'{nombre} no encontrado en el pedido')

    def calcular_subtotal(self):
        subtotal = 0
        for producto in self.productos:
            subtotal += producto.precio
        return subtotal

    def calcular_iva(self):
        return self.calcular_subtotal() * 0.15

    def calcular_total(self):
        return f'El total es {self.calcular_subtotal() + self.calcular_iva()}'


producto1 = Producto('Coca Cola', 3.25)
producto2 = Producto('Chito', 0.5)
producto3 = Producto('Polito', 0.25)
pedido = Pedido()
pedido.agregar_producto(producto1)
pedido.agregar_producto(producto2)
pedido.agregar_producto(producto3)
pedido.calcular_subtotal()
pedido.calcular_iva()
pedido.calcular_total()










