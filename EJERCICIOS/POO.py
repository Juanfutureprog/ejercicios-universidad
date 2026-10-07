# class Animal1:
#     def __init__(self,nombre,especie,edad):
#         self.nombre=nombre
#         self.especie=especie
#         self.edad=edad
#     def describir(self):
#         print(f"Hola, soy {self.nombre}, soy un {self.especie} y tengo {self.edad}")
#
# objeto1= Animal1("Peluche","perro",4)
# objeto2= Animal1("Mufasa","gato",2)
# objeto1.describir()
# objeto2.describir()
#
# class CuentaBancaria:
#     def __init__(self,titular,saldo):
#         self.titular=titular
#         self.saldo=saldo
#     def depositar(self,cantidad):
#         self.saldo=self.saldo + cantidad
#         print(f"Depositaste ${cantidad}, saldo actual: ${self.saldo}")
#     def retirar(self,cantidad):
#         if cantidad > self.saldo:
#             print("Saldo insuficiente")
#         else:
#             self.saldo=self.saldo-cantidad
#             print(f"Retiraste ${cantidad}, saldo actual: ${self.saldo}")
#     def ver_saldo(self):
#         print(f"Titular: {self.titular}, Saldo: ${self.saldo}")
#
# persona1= CuentaBancaria("Juan",1000)
# persona2= CuentaBancaria("Maria",500)
# persona1.depositar(200)
# persona2.retirar(100)
# persona1.ver_saldo()
# persona2.ver_saldo()
#
#
#
#
# computadora= {'pulgadas': 15.6, 'marca':'Lenovo','anio': 2020,'perifericos':['teclado''mouse']}
# televisor= {'color': 'negro', 'marca':'Samsung','anio': 2026,'pulgadas': 15.6}
# pizarra={'color': 'blanco', 'forma':'Rectangular','dimensiones':{'alto':60,'largo':100}}
#
# #habitacion
# cama={'plaza':2, 'material': 'madera', 'color':'negro'}
# ropero= {'color': 'cafe','dimensiones': [180,150], 'perifericos':'(cajones)'}
#
#
# personaje={'personaje1': 'Kelly', 'personaje2': 'Alok', 'personaje3': 'Orion'}
# maps={'maps1':'Purgatorio', 'maps2':'Bermuda', 'maps3':'Kalahari'}
# modos={'mod1':'Duelo de escuadras','mod2':'Entrenamiento', 'mod3': 'Clasificatorio'}
# armas={'arma1':'AK', 'arma2': 'Thompson', 'arma3': 'MP40'}
# delivery
# banco1= {'banco': 'Pichincha'}
# banco2= {'banco': 'Guayaquil'}
# banco3= {'banco': 'BGR'}
#
# metodo_de_pago={'metodo1':'Efectivo', 'metodo2':'Trasferencia'}
# local={'nombre':'KFC', 'direccion': 'Av Luis Lopez', 'Tiempo_espera': 20, 'hora_apertura':10,'hora_cierre': 23}


# class Local:
#     def __init__(self, nombre, direccion, Tiempo_espera, tipo_comida, hora_apertura, hora_cierre):
#         self.nombre = nombre
#         self.direccion = direccion
#         self.Tiempo_espera = Tiempo_espera
#         self.tipo_comida = tipo_comida
#         self.hora_apertura = hora_apertura
#         self.hora_cierre = hora_cierre
#     def __str__(self):
#         return f'{self.nombre},{self.direccion}'
#
# class Colaborador:
#     def __init__(self, nacionalidad, tipo_de_vehiculo, celular, nombre):
#         self.nacionalidad = nacionalidad
#         self.tipo_de_vehiculo = tipo_de_vehiculo
#         self.celular = celular
#         self.nombre = nombre
#     def __str__(self):
#         return f'{self.nacionalidad}'
#
# local3=Local('Rukito', 'Aventura Plaza', 12,'Asado', 22, 65)
# local4=Local('Pizza Hut', 'Paseo Shopping', 10, 'Asado', 22,24)
# colaborador2=Colaborador('Ecuatoriana', 'carro', "8868659540", 'Ariana')
# print(colaborador2)
# print(local3)
# print(local4)

#--------Herencia-------
# La herencia es cuando una clase hereda los atributos y métodos de otra clase.
# Sirve para reutilizar código sin repetirlo.
#Se define poniendo el nombre de la clase padre entre paréntesis:
#
# class Animal:                    # clase padre
#     def __init__(self, nombre, edad):
#         self.nombre = nombre
#         self.edad = edad
#
#     def describir(self):
#         print(f"Soy {self.nombre} y tengo {self.edad} años")
#
# class Perro(Animal):             # clase hija, hereda de Animal
#     def ladrar(self):
#         print(f"{self.nombre} dice: Guau!")
#
# class Gato(Animal):              # clase hija, hereda de Animal
#     def maullar(self):
#         print(f"{self.nombre} dice: Miau!")
#
# perro = Perro("Luna", 8)
# perro.describir()   # heredado de Animal
# perro.ladrar()      # propio de Perro
#
# gato = Gato("Mochi", 3)
# gato.describir()    # heredado de Animal
# gato.maullar()      # propio de Gato

# class Vehiculo:
#     def __init__(self,marca,modelo,velocidad_maxima):
#         self.marca= marca
#         self.modelo=modelo
#         self.velocidad_maxima=velocidad_maxima
#
#     def describir(self):
#         print(f'Soy un {self.marca} {self.modelo} con velocidad maxima de {self.velocidad_maxima} km/h')
#
# class Auto(Vehiculo):
#     def tipo(self):
#         print('Soy un auto de 4 ruedas')
#
# class Moto(Vehiculo):
#     def tipo(self):
#         print('Soy una moto de 2 ruedas')
#
# auto= Auto('Chevrolet', 'D-Max', 250)
# auto.describir()
# auto.tipo()
#
# moto= Moto('Honda', 'Civic', 150)
# moto.describir()
# moto.tipo()

#-----Nuevo concepto: super()---
# Hay veces que la clase hija necesita sus
# propios atributos adicionales además de los del padre. Para eso usamos super()
# class Animal:
#     def __init__(self, nombre, edad):
#         self.nombre = nombre
#         self.edad = edad
#
# class Perro(Animal):
#     def __init__(self, nombre, edad, raza):
#         super().__init__(nombre, edad)  # llama al __init__ del padre
#         self.raza = raza               # atributo propio de Perro
#
# perro = Perro("Luna", 8, "Schnauzer")
# print(perro.nombre)  # Luna
# print(perro.raza)    # Schnauzer

# class Persona:
#     def __init__(self, nombre, edad):
#         self.nombre= nombre
#         self.edad= edad
#
#     def presentarse(self):
#         print(f'Hola, me llamo {self.nombre} y tengo {self.edad} años')
#
# class Estudiante(Persona):
#     def __init__(self, nombre, edad, carrera):
#         super().__init__(nombre,edad)
#         self.carrera= carrera
#
#     def estudiar(self):
#         print(f'{self.nombre} está estudiando {self.carrera}')
#
# estudiante= Estudiante('Juan', 20, 'Igenieria de software')
# estudiante.presentarse()
# estudiante.estudiar()
#
#
#
# class Empleado:
#     def __init__(self, nombre, salario):
#         self.nombre= nombre
#         self.salario= salario
#
#     def presentarse(self):
#         print(f'Soy {self.nombre} y mi salario es ${self.salario}')
#
# class Gerente(Empleado):
#     def __init__(self, nombre, salario, departamento):
#         super().__init__(nombre,salario)
#         self.departamento= departamento
#
#     def info(self):
#         print(f'{self.nombre} es gerente del departamento de {self.departamento}')
#
# class Vendedor(Empleado):
#     def __init__(self, nombre, salario, comision):
#         super().__init__(nombre, salario)
#         self.comision= comision
#
#     def info(self):
#         print(f'{self.nombre} es vendedor y gana ${self.comision}')
#
# empleado= Empleado('Kevin', 500)
# gerente= Gerente('Axel', 1000, 'Recursos Humanos')
# vendedor= Vendedor('Ariana', 800, 200)
# empleado.presentarse()
# gerente.info()
# vendedor.info()
#
#
# class Producto:
#     def __init__(self,nombre,precio,estock):
#         self.nombre=nombre
#         self.precio=precio
#         self.stock=estock
#
#     def aplicar_descuento(self,porcentaje):
#         self.precio= self.precio - (self.precio * porcentaje/100)
#         print(f'Nuevo precio de {self.nombre} es {self.precio}')
#
#     def __str__(self):
#         return f'Producto:{self.nombre} Precio:{self.precio} Stock:{self.stock}'
#
# producto= Producto('Ariana', 1000000, 1)
# print(producto)
# producto.aplicar_descuento(50)
# print(producto)
#
#
# class Paciente:
#     def __init__(self, nombre, dni, ubicacion):
#         self.nombre= nombre
#         self.dni= dni
#         self.ubicacion= ubicacion
#         self.historial_clinico= []
#     def __str__(self):
#         return f'Nombre:{self.nombre} DNI:{self.dni} Ubicacion:{self.ubicacion} Historial Clinico:{self.historial_clinico}'
#
#
# class HistorialClinico:
#     def __init__(self,fecha, enfermedad, medico_asignado):
#         self.fecha= fecha
#         self.enfermedad= enfermedad
#         self.medico_asignado= medico_asignado
#     # def __repr__(self):
#     #     return f'Fecha: {self.fecha} | Enfermedad: {self.enfermedad} | Medico: {self.medico_asignado}'
#     def __str__(self):
#         return f'Fecha: {self.fecha} | Enfermedad: {self.enfermedad} | Medico: {self.medico_asignado}'
#     def __repr__(self):
#         return self.__str__()
#
# paciente1= Paciente('Ariana Ortega', '1234567890', 'Calle 22')
# historial1= HistorialClinico('2023-01-01', 'Diabetes', 'Dr. Juan Perez')
# paciente1.historial_clinico.append(historial1)
# print(paciente1)
#
# class Ambulancia:
#     def __init__(self,can_pasajeros, placa):
#         self.nombre= 'Ambulancia'
#         self.accesorios = []
#         self.can_pasajeros = can_pasajeros
#         self.placa = placa
#     def __str__(self):
#         return f'{self.nombre}, {self.placa},accesorios: {self.accesorios}'
#
# class Equipo:
#     def __init__(self, tipo, nombre, bateria):
#         self.tipo= tipo
#         self.nombre= nombre
#         self.bateria= bateria
#     def __repr__(self):
#         return f'{self.tipo}, {self.nombre}, {self.bateria}'
#
#
# ambulancia_1= Ambulancia(5, 'GBV-2020')
# equipo1= Equipo('Electronico', 'Desfribilador', 100)
# ambulancia_1.accesorios.append(equipo1)
# print(ambulancia_1)
# for i in range(len(ambulancia_1.accesorios)):
#     print(ambulancia_1.accesorios[i])
#
# class Enfermedad:
#     def __init__(self, nombre, codigo, tipo):
#         self.nombre= nombre
#         self.codigo= codigo
#         self.tipo= tipo
#         self.medicamentos= []
#     def __str__(self):
#         return f'Nombre: {self.nombre} Codigo: {self.codigo} Tipo: {self.tipo} Medicamentos: {self.medicamentos}'
#
# class Medicamento:
#     def __init__(self, nombre, marca, precio, disponibilidad):
#         self.nombre= nombre
#         self.marca= marca
#         self.precio= precio
#         self.disponibilidad= disponibilidad
#
#     def __str__(self):
#         return f'Nombre: {self.nombre} Marca: {self.marca} Precio: {self.precio} Disponibilidad: {self.disponibilidad}'
#     def __repr__(self):
#         return self.__str__()
#
# enfermedad1= Enfermedad('Diabetes', 'CIE-11', 'Metabólica y Crónica')
# medicamento1= Medicamento('Insulina', 'Bayer', 100, True)
# enfermedad1.medicamentos.append(medicamento1)
# print(enfermedad1)
#
#
#
# class Libro:
#     def __init__(self, titulo, autor):
#         self.titulo= titulo
#         self.autor=autor
#
#     def __str__(self):
#         return f'Titulo:{self.titulo} Autor:{self.autor}'
#
# class Biblioteca:
#     def __init__(self,nombre,libros):
#         self.nombre=nombre
#         self.libros=libros
#
#     def agregar_libro(self,libro):
#         self.libros.append(libro)
#
#     def mostrar_libros(self):
#         for libro in self.libros:
#             print(f'Titulo:{libro.titulo} Autor:{libro.autor}')
#
# libro1 = Libro("Harry Potter", "J.K. Rowling")
# libro2 = Libro("El Principito", "Antoine de Saint-Exupery")
# libro3 = Libro("Cien Anos de Soledad", "Gabriel Garcia Marquez")
#
# biblioteca = Biblioteca("Mi Biblioteca", [])
#
# biblioteca.agregar_libro(libro1)
# biblioteca.agregar_libro(libro2)
# biblioteca.agregar_libro(libro3)
#
# biblioteca.mostrar_libros()
#
#
# class UtilEscolar:
#     def __init__(self, marca, tipo,tamaño):
#         self.marca= marca
#         self.tipo= tipo
#         self.tamaño= tamaño
#
# class Cuaderno(UtilEscolar):
#     def __init__(self, marca, tipo, tamaño, cant_hojas):
#         super().__init__(marca, tipo, tamaño)
#         self.cant_hojas= cant_hojas
#
#     def __str__(self):
#         return f'Marca: {self.marca}, Tipo: {self.tipo}, Tamaño: {self.tamaño}, Cantidad de hojas: {self.cant_hojas}'
#
#
# class Esfero(UtilEscolar):
#     def __init__(self, marca, tipo, tamaño,  color_tinta, punta):
#         super().__init__(marca, tipo, tamaño)
#         self.color_tinta= color_tinta
#         self.punta= punta
#
#     def __str__(self):
#         return f'Marca: {self.marca}, Tipo: {self.tipo}, Tamaño: {self.tamaño}, Color: {self.color_tinta}, {self.punta}'
#
#
# class Calculadora(UtilEscolar):
#     def __init__(self, marca, tipo, tamaño, color, modelo):
#         super().__init__(marca, tipo, tamaño)
#         self.color= color
#         self.modelo= modelo
#
#     def __str__(self):
#         return f'Marca: {self.marca}, Tipo: {self.tipo}, Tamaño: {self.tamaño}, Color: {self.color}, {self.modelo}'
#
#
# cuaderno= Cuaderno('Norma', 'Cocido', 'Grande', 100)
# esfero= Esfero('Norma', 'Plastica', 'Pequeña', 'Roja', 'Fina')
# calculadora= Calculadora('CASIO', 'Cientifica', 'Mediana','Celeste', 'Casio fx-991SP CW')
# print(cuaderno)
# print(esfero)
# print(calculadora)
#
#
# class Vehiculo:
#     def describir(self):
#         print('Soy un vehiculo')
#
# class Auto(Vehiculo):
#     def describir(self):
#         print('Soy un auto de 4 ruedas')
#
# class Moto(Vehiculo):
#     def describir(self):
#         print('Soy una moto de 2 ruedas')
#
# class Camion(Vehiculo):
#     def describir(self):
#         print('Soy un camion de carga')
#
#
# vehiculo= Vehiculo()
# vehiculo.describir()
# auto= Auto()
# auto.describir()
# moto= Moto()
# moto.describir()
# camion= Camion()
# camion.describir()
#
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
#sobreescribir
#Se refiere a modificar o sustituir el comportamiento predeterminado de un
# método heredado en lenguajes orientados a objetos (polimorfismo)
# En programación, redefinir (conocido como override) es la capacidad que tiene una clase hija (subclase)
# de proveer una implementación específica para un método que ya fue definido en su clase padre (superclase).
# Esto significa que el método mantiene el mismo nombre y parámetros, pero realiza una acción distinta.
# class Figura:
#     def __init__(self, nombre):
#         self.nombre= nombre
#
#     def area(self):
#         print('No se puede calcular el area')
#
#     def __str__(self):
#         return f'Figura : {self.nombre}'
#
# class Cuadrado(Figura):
#     def __init__(self, nombre, lado):
#         super().__init__(nombre)
#         self.lado= lado
#
#     def area(self):
#         area= self.lado * self.lado
#         print(f'El area del cuadrado es {area}')
#
# class Circulo(Figura):
#     def __init__(self, nombre, radio):
#         super().__init__(nombre)
#         self.radio= radio
#
#     def area(self):
#         area= 3.14 * (self.radio ** 2)
#         print(f'El area del circulo es {area}')
#
# figura1= Figura('cuadrado')
# figura2= Cuadrado('cuadrado', 5)
# figura3= Circulo('circulo', 5)
# print(figura1)
# figura1.area()
# figura2.area()
# figura3.area()
#
#
# class Empleado:
#     def __init__(self, nombre, horas_trabajadas):
#         self.nombre= nombre
#         self.horas_trabajadas= horas_trabajadas
#
#     def calcular_pago(self):
#         pago= self.horas_trabajadas * 10
#         print(f'{self.nombre} y gano ${pago}')
#         return pago
#
# class Empleado_fijo(Empleado):
#     def calcular_pago(self):
#         salario_fijo= 800
#         print(f' {self.nombre} gano ${salario_fijo} ')
#         return salario_fijo
#
# class EmpleadoPorHora(Empleado):
#     def __init__(self, nombre, horas_trabajadas, tarifa_hora):
#         super().__init__(nombre,horas_trabajadas)
#         self.tarifa_hora= tarifa_hora
#
#     def calcular_pago(self):
#         pago= self.horas_trabajadas * self.tarifa_hora
#         print(f' {self.nombre} gano ${pago}')
#         return pago
#
# class Empresa:
#     def __init__(self, nombre):
#         self.nombre= nombre
#         self.empleados= []
#
#     def contratar(self, empleado):
#         self.empleados.append(empleado)
#
#     def nomina_total(self):
#         total= 0
#         for i in self.empleados:
#             total+= i.calcular_pago()
#         print(f'La nomina total es ${total}')
#
# empresa= Empresa('Google')
# empleado1= Empleado('Ariana', 8)
# empleado2= Empleado_fijo('Axel', 12)
# empleado3= EmpleadoPorHora('Juan', 10, 8)
# empresa.contratar(empleado1)
# empresa.contratar(empleado2)
# empresa.contratar(empleado3)
# empresa.nomina_total()
#
#
#
# class Videojuegos:
#     def __init__(self, titulo, genero, precio):
#         self.titulo= titulo
#         self.genero= genero
#         self.precio= precio
#
#     def aplicar_descuento(self, porcentaje):
#         self.precio= self.precio - (self.precio * porcentaje/100)
#         return self.precio
#
#     def __str__(self):
#         return f'{self.titulo} - {self.genero} - {self.precio}'
#
# class Tienda:
#     def __init__(self, nombre):
#         self.nombre= nombre
#         self.inventario= []
#
#     def agregar_juego(self, juego):
#         self.inventario.append(juego)
#
#     def mostrar_inventario(self):
#         for juego in self.inventario:
#             print(juego)
#
#     def aplicar_descuento(self, procentaje):
#         for juego in self.inventario:
#             juego.aplicar_descuento(procentaje)
#
# juego1= Videojuegos('Warzone', ' battle royale', 100)
# juego2= Videojuegos('Fornite', ' battle royale', 90)
# juego3= Videojuegos('League of Legends', ' shooter', 120)
# tienda= Tienda('PlayStation')
# tienda.agregar_juego(juego1)
# tienda.agregar_juego(juego2)
# tienda.agregar_juego(juego3)
# tienda.mostrar_inventario()
# tienda.aplicar_descuento(10)
# tienda.mostrar_inventario()
#
#
# class Estudiante:
#     def __init__(self, nombre):
#         self.nombre= nombre
#         self.notas= []
#
#     def agregar_nota(self, nota):
#         self.notas.append(nota)
#
#     def calcular_promedio(self):
#         promedio= sum(self.notas) / len(self.notas)
#         return promedio
#
#     def __str__(self):
#         return f'{self.nombre} - Promedio: {self.calcular_promedio()}'
#
# class Salon:
#     def __init__(self, grado):
#         self.grado= grado
#         self.estudiantes= []
#
#     def agregar_estudiante(self, estudiante):
#         self.estudiantes.append(estudiante)
#
#     def mostrar_promedios(self):
#         for estudiante in self.estudiantes:
#             print(estudiante)
#
#     def mejor_estudiante(self):
#         mejor = None
#         for estudiante in self.estudiantes:
#             if mejor is None or estudiante.calcular_promedio() > mejor.calcular_promedio():
#                 mejor = estudiante
#         return mejor
#
# ariana= Estudiante('Ariana')
# ariana.agregar_nota(10)
# ariana.agregar_nota(9)
# ariana.agregar_nota(8)
# axel= Estudiante('Axel')
# axel.agregar_nota(7)
# axel.agregar_nota(6)
# axel.agregar_nota(5)
# juan= Estudiante('Juan')
# juan.agregar_nota(8)
# juan.agregar_nota(9)
# juan.agregar_nota(7)
# salon1= Salon('A')
# salon1.agregar_estudiante(ariana)
# salon1.agregar_estudiante(axel)
# salon1.agregar_estudiante(juan)
# salon1.mostrar_promedios()
# salon1.mejor_estudiante()
# print(salon1.mejor_estudiante())

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
#
#
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
#
#
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

# class Figura:
#     def cal_perimetro(self):
#         print('No se puede calcular el perimetro')
#
#     def cal_area(self):
#         print('No se puede calcular el area')
#
#
# class Rectangulo(Figura):
#     def __init__(self, ancho, largo):
#         self.ancho = ancho
#         self.largo = largo
#
#     def cal_perimetro(self):
#         perimetro = (2 * self.largo) + (2 * self.ancho)
#         print(f' El perimetro del rectangulo es {perimetro}')
#
#     def cal_area(self):
#         area = self.largo * self.ancho
#         print(f' El area del rectangulo es {area}')
#
#
# class Circulo(Figura):
#     def __init__(self, radio):
#         self.radio = radio
#
#     def cal_perimetro(self):
#         perimetro = 2 * 3.14 * self.radio
#         print(f' El perimetro del circulo es {perimetro}')
#
#     def cal_area(self):
#         area = 3.14 * (self.radio ** 2)
#         print(f' El area del circulo es {area}')
#
#
# class Triangulo(Figura):
#     def __init__(self, lado1, lado2, lado3, base, altura):
#         self.lado1 = lado1
#         self.lado2 = lado2
#         self.lado3 = lado3
#         self.base = base
#         self.altura = altura
#
#
#     def cal_perimetro(self):
#          perimetro = self.lado1 + self.lado2 + self.lado3
#          print(f'El perimetro de su triangulo es {perimetro}')
#
#     def cal_area(self):
#         area = (self.base * self.altura) / 2
#         print(f'El area de su triangulo es {area}')
#
#
# figuras = [Rectangulo(10, 5), Circulo(10), Triangulo(7, 8, 5, 7, 4)]
# for figura in figuras:
#     figura.cal_perimetro()
#
# for figura in figuras:
#     figura.cal_area()

# class Producto:
#     def __init__(self, codigo, nombre, precio, stock):
#         self.codigo = codigo
#         self.nombre = nombre
#         self.precio = precio
#         self.stock = stock
#
#     def __str__(self):
#         return f'Codigo: {self.codigo}, Nombre: {self.nombre}, Precio: {self.precio}, Stock: {self.stock}'
#
# class Inventario:
#     def __init__(self):
#         self.productos = []
#
#     def agregar_producto(self, producto):
#         self.productos.append(producto)
#
#     def eliminar_stock(self, nombre, cantidad):
#         for producto in self.productos:
#             if producto.nombre == nombre:
#                 if producto.stock >= cantidad:
#                     producto.stock -= cantidad
#                     print(f'Stock del producto {nombre} actualizado, stock actual: {producto.stock}')
#                 else:
#                     print(f'No hay stock suficiente para reabastecer el producto {nombre}')
#                 return
#
#         print(f'El producto {nombre} no se encuentra en el inventario')
#
#     def reabastecer_stock(self, nombre,cantidad):
#         for producto in self.productos:
#             if producto.nombre == nombre:
#                 producto.stock += cantidad
#                 print(f'Stock del producto {nombre} actualizado, stock actual: {producto.stock}')
#                 return
#         print(f'El producto {nombre} no se encuentra en el inventario')
#
#     def mostrar_productoos(self):
#         for producto in self.productos:
#             print(producto)
#
#     def calcular_total(self):
#         total=0
#         for producto in self.productos:
#             total += producto.precio * producto.stock
#         return f'El total de la compra es: {total}'
#
# producto1= Producto(123, 'Oreo', 1, 20)
# producto2= Producto(145, 'Coca Cola', 1.25, 15)
# producto3= Producto(165, 'Fideo', 0.45, 12)
# producto4= Producto(185, 'Chocolate', 2.50, 0)
# inventario= Inventario()
# inventario.agregar_producto(producto1)
# inventario.agregar_producto(producto2)
# inventario.agregar_producto(producto3)
# inventario.agregar_producto(producto4)
# inventario.eliminar_stock('Oreo', 5)
# inventario.eliminar_stock('Coca Cola', 6)
# inventario.eliminar_stock('Fideo', 2)
# inventario.eliminar_stock('Chocolate', 1)
# inventario.reabastecer_stock('Oreo', 20)
# inventario.mostrar_productoos()
# print(inventario.calcular_total())

# class Deportista:
#     def __init__(self, nombre, edad, nacionaliad, altura,
#                  peso, equipo, numero_camiseta, anios_experiencia, salario, lesionado,
#                  id_deportista):
#         self.nombre = nombre
#         self.edad = edad
#         self.nacionaliad = nacionaliad
#         self.altura = altura
#         self.peso = peso
#         self.equipo = equipo
#         self.numero_camiseta = numero_camiseta
#         self.anios_experiencia = anios_experiencia
#         self.salario = salario
#         self.lesionado = lesionado
#         self.id_deportista = id_deportista
#
#     def presentarse(self):
#         print(f'Soy {self.nombre}, tengo {self.edad} y juego para '
#               f'{self.equipo} con el número {self.numero_camiseta}')
#
#     def actualizar_salario(self, aumento):
#         self.salario += aumento
#         print(f'{self.nombre} recibió un aumento de ${aumento:.2f}. '
#               f'Salario actual: ${self.salario}')
#
#     def entrenar(self):
#         print(f'{self.nombre} está realizando un entrenamiento general')
#
#
# class Futbolista(Deportista):
#     def __init__(self, nombre, edad, nacionaliad, altura,
#                  peso, equipo, numero_camiseta, anios_experiencia, salario, lesionado,
#                  id_deportista, posicion, goles_anotados, asistencias,
#                  tarjetas_amarillas, pie_habil):
#         super().__init__(nombre, edad, nacionaliad, altura,
#                          peso, equipo, numero_camiseta, anios_experiencia, salario, lesionado,
#                          id_deportista)
#
#         self.posicion = posicion
#         self.goles_anotados = goles_anotados
#         self.asistencias = asistencias
#         self.tarjetas_amarillas = tarjetas_amarillas
#         self.pie_habil = pie_habil
#
#     # 👇 Ahora sí están alineados con def __init__
#     def anotar_gol(self):
#         self.goles_anotados += 1
#         print(f'¡Gooool de {self.nombre}! '
#               f'Lleva {self.goles_anotados} goles anotados en el partido')
#
#     def hacer_falta(self):
#         self.tarjetas_amarillas += 1
#         print(f'{self.nombre} ha hecho una falta. '
#               f'Recibió una tarjeta amarilla. '
#               f'Total de tarjetas amarillas: {self.tarjetas_amarillas}')
#
#     def entrenar(self):
#         super().entrenar()
#         print(f'El jugador {self.nombre} entrena tiros a puerta y resistencia '
#               f'para poder jugar como {self.posicion}')
#
#
# class Basquetbolista(Deportista):
#     def __init__(self, nombre, edad, nacionaliad, altura,
#                  peso, equipo, numero_camiseta, anios_experiencia, salario, lesionado,
#                  id_deportista, puntos_anotados, rebotes, numero_triples,
#                  mano_habil, numero_faltas):
#         super().__init__(nombre, edad, nacionaliad, altura,
#                          peso, equipo, numero_camiseta, anios_experiencia, salario, lesionado,
#                          id_deportista)
#
#         self.puntos_anotados = puntos_anotados
#         self.rebotes = rebotes
#         self.numero_triples = numero_triples
#         self.mano_habil = mano_habil
#         self.numero_faltas = numero_faltas
#
#     # 👇 También alineados con def __init__
#     def anotar_puntos(self, puntos):
#         self.puntos_anotados += puntos
#         print(f'{self.nombre} anota {puntos} puntos. '
#               f'Lleva {self.puntos_anotados} en el partido')
#
#     def capturar_rebotes(self):
#         self.rebotes += 1
#         print(f'{self.nombre} captura un rebote. '
#               f'Total de rebotes: {self.rebotes}')
#
#     def entrenar(self):
#         super().entrenar()
#         print(f'El jugador {self.nombre} entrena lanzamiento de triples '
#               f'y ejercicios de saltos')
#
#
# futbolista1 = Futbolista('Mesi', 39, 'Argentina', 1.70, 67, 'Inter Miami',
#                          10, 21, 500000, False, 'F001',
#                          'Delantero', 0, 0, 0, 'Izquierdo')
# futbolista1.anotar_gol()
# futbolista1.hacer_falta()
# futbolista1.entrenar()
# futbolista1.actualizar_salario(25000)

class Deportista:
    def __init__(self, nombre, edad, nacionalidad, altura, peso,
                equipo, numero_camiseta, anios_experiencia, salario, lesionado,
                id_deportista):
        self.nombre= nombre
        self.edad= edad
        self.nacionalidad= nacionalidad
        self.altura= altura
        self.peso= peso
        self.equipo= equipo
        self.numero_camiseta= numero_camiseta
        self.anios_experiencia= anios_experiencia
        self.salario= salario
        self.lesionado= lesionado
        self.id_deportista= id_deportista

    def presentarse(self):
        print(f'Soy {self.nombre}, tengo {self.edad} años,'
              f'juego para {self.equipo} con el número {self.numero_camiseta}')

    def actualizar_salario(self, aumento):
        self.salario+= aumento
        print(f'El jugador {self.nombre} ha recibido un aumento ${aumento:.2f}.'
              f'Salario actual {self.salario:.2f}')

    def entrenar(self):
        print(f'El deportista {self.nombre} esta haciendo un entrenamiento general ')


class Futbolista(Deportista):
    def __init__(self, nombre, edad, nacionalidad, altura, peso,
                equipo, numero_camiseta, anios_experiencia, salario, lesionado,
                id_deportista, posicion,goles_anotados, asistencias, tarjetas_amarilas,
                pie_habil):
        super().__init__(nombre, edad, nacionalidad, altura, peso,
                equipo, numero_camiseta, anios_experiencia, salario, lesionado,
                id_deportista)
        self.posicion= posicion
        self.goles_anotados= goles_anotados
        self.asistencias= asistencias
        self.tarjetas_amarillas= tarjetas_amarilas
        self.pie_habil= pie_habil

    def anotar_gol(self):
        self.goles_anotados+= 1
        print(f'Goooool de {self.nombre}.'
              f'Lleva {self.goles_anotados} goles anotados en el partido.')

    def hacer_falta(self):
        self.tarjetas_amarillas+= 1
        print(f'El jugador a hecho una falta, recibe tarjeta amarilla.'
              f'Regista {self.tarjetas_amarillas} tarjetas amarillas en el partido')

    def entrenar(self):
        super().entrenar()
        print(f'El jugador {self.nombre} esta realizando tiros a puerta y'
              f' ejercicios de velocidad')

class Basquetbolista(Deportista):
    def __init__(self, nombre, edad, nacionalidad, altura, peso,
                 equipo, numero_camiseta, anios_experiencia, salario, lesionado,
                 id_deportista, puntos_anotados, rebotes, numero_triples,
                 numero_faltas, mano_habil):
        super().__init__(nombre, edad, nacionalidad, altura, peso,
                         equipo, numero_camiseta, anios_experiencia, salario, lesionado,
                         id_deportista)
        self.puntos_anotados= puntos_anotados
        self.rebotes= rebotes
        self.numero_triples = numero_triples
        self.numero_faltas= numero_faltas
        self.mano_habil= mano_habil

    def anotar_puntos(self, puntos):
        self.puntos_anotados+= puntos
        print(f'El jugador {self.nombre} ha hecho {puntos} puntos.'
              f'Lleva un total de {self.puntos_anotados} en el partido')

    def capturar_rebotes(self):
        self.rebotes+= 1
        print(f'{self.nombre} captura un rebote.'
              f'Total de rebotes en el partido: {self.rebotes}')

    def entrenar(self):
        super().entrenar()
        print(f'El jugador se encuentra realizando ejercicios de saltos y '
              f'lanzamientos de triples')

fut1= Futbolista('Messi',39, 'Argentina', 1.70, 67, 'Inter Miami',
                 10, 21, 500000, False, 'F001',
                 'Delantero', 0,0,0,'Izquierdo')
fut1.anotar_gol()
fut1.hacer_falta()
fut1.entrenar()
print('=='*80)
bast= Basquetbolista('Michael Jordan',40, 'Estadounidense', 1.98, 98, 'Chicago Bulls',
                 23, 15, 200000, False, 'B001',
                 0, 0,0,0,'Derecha')
bast.anotar_puntos(9)
bast.capturar_rebotes()
bast.entrenar()
























