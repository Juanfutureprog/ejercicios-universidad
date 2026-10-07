class Deportista:
    def __init__(self,nombre, edad, nacionalidad,altura, peso,
                 equipo, numero_camiseta, anios_experiencia, salario,
                 lesionado, id_deportista):
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
        print(f'Mi nombre es {self.nombre}, tengo{self.años}.'
              f'Estoy en el equipo {self.equipo} con el numero {self.numero_camiseta}')

    def actualizar_salario(self, aumento):
        self.salario += aumento
        print(f'El deportista {self.nombre} recibio un aumento de {aumento} dolares.'
              f'Su salario actual es de {self.salario} dolares')

    def entrenar(self):
        print(f'El deportista {self.nombre} se encuentra realizando un entrenamiento general')

class Futbolista(Deportista):
    def __init__(self, nombre, edad, nacionalidad, altura, peso,
                 equipo, numero_camiseta, anios_experiencia, salario,
                 lesionado, id_deportista, posicion, goles_anotados,
                 asistencias, tarjetas_amarillas, pie_habil):
        super().__init__(nombre, edad, nacionalidad, altura, peso,
                 equipo, numero_camiseta, anios_experiencia, salario,
                 lesionado, id_deportista)
        self.posicion= posicion
        self.goles_anotados= goles_anotados
        self.asistencias= asistencias
        self.tarjetas_amarillas= tarjetas_amarillas
        self.pie_habil= pie_habil

    def marcar_gol(self):
        self.goles_anotados+= 1
        print(f'Goool del jugador {self.nombre} con la camiseta numero {self.numero_camiseta}.'
              f'El jugar lleva {self.goles_anotados} goles anotados.')

    def hacer_falta(self):
        self.tarjetas_amarillas+= 1
        print(f'El jugador {self.nombre} a hecho una falta, recibe una tarjeta amarilla.'
              f'El jugador registra {self.tarjetas_amarillas} tarjets amarillas en el partido.')

    def entrenar(self):
        super().entrenar()
        print(f'El jugador {self.nombre} esta  realizando tiros puerta y ejercicios de fuerza ')

class Basquetbolista(Deportista):
    def __init__(self, nombre, edad, nacionalidad, altura, peso,
                 equipo, numero_camiseta, anios_experiencia, salario,
                 lesionado, id_deportista, puntos_anotados, rebotes, numero_triples,
                 mano_habil, numero_faltas):
        super().__init__(nombre, edad, nacionalidad, altura, peso,
                 equipo, numero_camiseta, anios_experiencia, salario,
                 lesionado, id_deportista)

        self.puntos_anotados= puntos_anotados
        self.rebotes= rebotes
        self.numero_triples= numero_triples
        self.mano_habil= mano_habil
        self.numero_faltas= numero_faltas

    def anotar_puntos(self, puntos):
        self.puntos_anotados+= puntos
        print(f'El jugador {self.nombre} ha hecho {puntos} puntos.'
              f'Lleva un total de {self.puntos_anotados} en el partido')

    def capturar_rebote(self):
        self.rebotes+= 1
        print(f'El jugador {self.nombre} captura un rebote.'
              f'Lleva un total de {self.rebotes} rebotes en el partido')

    def entrenar(self):
        super().entrenar()
        print(f'El jugador {self.nombre} se encuentra realizando tiros triples y ejercicio de saltos')

futbolista1= Futbolista('Messi', 39, 'Argentina ', 1.70, 67, 'Inter de Miami',
                        10, 21, 600000, False, 'F001',
                        'Delantero', 0, 0, 0, 'Izquierdo')

futbolista1.marcar_gol()
futbolista1.hacer_falta()
futbolista1.entrenar()
futbolista1.actualizar_salario(50000)
print('=='* 70)
basquetbolista1=Basquetbolista('Michael Jordan', 40, 'Estadounidense ',
                               1.98, 90, 'Chicago Bulls',
                        23, 15, 400000, False, 'B001',
                        0, 0, 0, 0, 'Derecha')

basquetbolista1.anotar_puntos(6)
basquetbolista1.capturar_rebote()
basquetbolista1.entrenar()
basquetbolista1.actualizar_salario(10000)




