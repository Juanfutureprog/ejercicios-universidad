class Deportista:
    def __init__(self, nombre, edad, nacionalidad, altura, peso, equipo,
                 numero_camiseta, anios_experiencia, salario, lesionado,
                 id_deportista):

        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        self.altura = altura
        self.peso = peso
        self.equipo = equipo
        self.numero_camiseta = numero_camiseta
        self.anios_experiencia = anios_experiencia
        self.salario = salario
        self.lesionado = lesionado
        self.id_deportista = id_deportista


    def presentarse(self):
        print(f"Soy {self.nombre}, tengo {self.edad} anios y juego para "
              f"{self.equipo} con el numero {self.numero_camiseta}.")


    def actualizar_salario(self, aumento):
        self.salario += aumento
        print(f"{self.nombre} ahora gana ${self.salario:.2f} "
              f"(aumento de ${aumento:.2f}).")


    def entrenar(self):
        print(f"{self.nombre} esta realizando un entrenamiento general.")



class Futbolista(Deportista):
    def __init__(self, nombre, edad, nacionalidad, altura, peso, equipo,
                 numero_camiseta, anios_experiencia, salario, lesionado,
                 id_deportista, posicion, goles_anotados, asistencias,
                 tarjetas_amarillas, pie_habil):
        super().__init__(nombre, edad, nacionalidad, altura, peso, equipo,
                         numero_camiseta, anios_experiencia, salario,
                         lesionado, id_deportista)
        self.posicion = posicion
        self.goles_anotados = goles_anotados
        self.asistencias = asistencias
        self.tarjetas_amarillas = tarjetas_amarillas
        self.pie_habil = pie_habil


    def anotar_gol(self):
        self.goles_anotados += 1
        print(f"¡Gol de {self.nombre}! Lleva {self.goles_anotados} goles.")

    def hacer_falta(self):
        self.tarjetas_amarillas += 1
        print(f"{self.nombre} recibe tarjeta amarilla. "
              f"Total: {self.tarjetas_amarillas}.")

    def entrenar(self):
        print(f"{self.nombre} entrena tiros a puerta y resistencia "
              f"para jugar como {self.posicion}.")



class Baloncestista(Deportista):
    def __init__(self, nombre, edad, nacionalidad, altura, peso, equipo,
                 numero_camiseta, anios_experiencia, salario, lesionado,
                 id_deportista, puntos_anotados, rebotes, numero_triples,
                 mano_habil, numero_faltas):
        super().__init__(nombre, edad, nacionalidad, altura, peso, equipo,
                         numero_camiseta, anios_experiencia, salario,
                         lesionado, id_deportista)
        self.puntos_anotados = puntos_anotados
        self.rebotes = rebotes
        self.numero_triples = numero_triples
        self.mano_habil = mano_habil
        self.numero_faltas = numero_faltas

    def anotar_puntos(self, puntos):
        self.puntos_anotados += puntos
        print(f"{self.nombre} anota {puntos} puntos. "
              f"Lleva {self.puntos_anotados} en el partido.")

    def capturar_rebote(self):
        self.rebotes += 1
        print(f"{self.nombre} captura un rebote. Total: {self.rebotes}.")

    def entrenar(self):
        print(f"{self.nombre} entrena lanzamientos de triples "
              f"y ejercicios de salto.")



# --- Creacion de objeto Futbolista ---
jugador1 = Futbolista(
    nombre="Lionel", edad=37, nacionalidad="Argentina", altura=1.70,
    peso=72, equipo="Inter Miami", numero_camiseta=10,
    anios_experiencia=20, salario=500000, lesionado=False,
    id_deportista="F001", posicion="Delantero", goles_anotados=0,
    asistencias=15, tarjetas_amarillas=0, pie_habil="Izquierdo"
)

# --- Creacion de objeto Baloncestista ---
jugador2 = Baloncestista(
    nombre="LeBron", edad=40, nacionalidad="Estados Unidos", altura=2.06,
    peso=113, equipo="Lakers", numero_camiseta=23,
    anios_experiencia=21, salario=700000, lesionado=False,
    id_deportista="B001", puntos_anotados=0, rebotes=0,
    numero_triples=0, mano_habil="Derecha", numero_faltas=0
)

# --- Ejecucion de metodos de jugador1 (Futbolista) ---
jugador1.presentarse()
jugador1.anotar_gol()
jugador1.hacer_falta()
jugador1.actualizar_salario(20000)
jugador1.entrenar()
print("\n" + "="*70)
# --- Ejecucion de metodos de jugador2 (Baloncestista) ---
jugador2.presentarse()
jugador2.anotar_puntos(3)
jugador2.capturar_rebote()
jugador2.actualizar_salario(15000)
jugador2.entrenar()
