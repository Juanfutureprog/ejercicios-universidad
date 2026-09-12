from abc import ABC, abstractmethod

# ==========================================
# 1. PATRÓN BUILDER (Construcción de Historia)
# ==========================================
class HistoriaClinica:
    def __init__(self):
        self.partes = []

    def agregar(self, parte):
        self.partes.append(parte)

    def mostrar_historia(self):
        print(f"Historia Clínica contiene: {', '.join(self.partes)}")

class IBuilderHistoria(ABC):
    @abstractmethod
    def build_paciente_info(self): pass
    @abstractmethod
    def build_diagnosticos(self): pass
    @abstractmethod
    def build_medicamentos(self): pass

class HistoriaBuilder(IBuilderHistoria):
    def __init__(self):
        self.reset()
    def reset(self):
        self._historia = HistoriaClinica()
    def build_paciente_info(self):
        self._historia.agregar("Datos Personales")
    def build_diagnosticos(self):
        self._historia.agregar("Diagnóstico Médico")
    def build_medicamentos(self):
        self._historia.agregar("Receta de Medicamentos")
    def get_resultado(self):
        historia = self._historia
        self.reset()
        return historia

class DirectorHospital:
    def __init__(self):
        self._builder = None
    def set_builder(self, builder: IBuilderHistoria):
        self._builder = builder
    def construir_historia_completa(self):
        self._builder.build_paciente_info()
        self._builder.build_diagnosticos()
        self._builder.build_medicamentos()

# ==========================================
# 2. PATRÓN TEMPLATE METHOD (Informes Médicos)
# ==========================================
class GeneradorInforme(ABC):
    def generar_informe(self):  # El "Template Method"
        self._escribir_encabezado()
        self.redactar_analisis_especialidad()
        self._firmar_documento()

    def _escribir_encabezado(self):
        print("--- INFORME MÉDICO ---")
    def _firmar_documento(self):
        print("Firma Autorizada: Dr. Hospital\n")

    @abstractmethod
    def redactar_analisis_especialidad(self): pass

class InformeCardiologia(GeneradorInforme):
    def redactar_analisis_especialidad(self):
        print("Análisis: Ritmo cardíaco estable, presión arterial normal.")

class InformePediatria(GeneradorInforme):
    def redactar_analisis_especialidad(self):
        print("Análisis: Paciente infantil presenta cuadro febril leve.")

# ==========================================
# 3. PATRÓN OBSERVER (Notificaciones)
# ==========================================
class IObservador(ABC):
    @abstractmethod
    def update(self, estado: str): pass

class SujetoPaciente:
    def __init__(self):
        self._observadores = []
        self._estado = ""

    def adjuntar(self, observador: IObservador):
        self._observadores.append(observador)

    def set_estado(self, estado: str):
        print(f"\n[SISTEMA] Estado del paciente actualizado a: {estado}")
        self._estado = estado
        self._notificar()

    def _notificar(self):
        for obs in self._observadores:
            obs.update(self._estado)

class MedicoTratante(IObservador):
    def update(self, estado: str):
        print(" -> Médico notificado: Revisar nuevo estado.")
class ModuloLaboratorio(IObservador):
    def update(self, estado: str):
        print(" -> Laboratorio notificado: Preparar nuevos exámenes.")

# ==========================================
# 4. PATRÓN PROXY (Seguridad de Acceso)
# ==========================================
class IHistoriaAcceso(ABC):
    @abstractmethod
    def acceder_historia(self, usuario: str, suscripcion: str): pass

class HistoriaReal(IHistoriaAcceso):
    def acceder_historia(self, usuario: str, suscripcion: str):
        print(f"Acceso Concedido: Mostrando historia clínica ultra-secreta al usuario {usuario}.")

class ProxyHistoriaPremium(IHistoriaAcceso):
    def __init__(self):
        self._historia_real = HistoriaReal()

    def acceder_historia(self, usuario: str, suscripcion: str):
        print(f"\nIntentando acceder con nivel: {suscripcion}...")
        if self._verificar_suscripcion(suscripcion):
            self._historia_real.acceder_historia(usuario, suscripcion)
        else:
            print("Acceso Denegado: Su nivel de suscripción no permite ver esta historia.")

    def _verificar_suscripcion(self, suscripcion: str) -> bool:
        return suscripcion == "Premium"

# ==========================================
# CÓDIGO CLIENTE (Prueba Funcional)
# ==========================================
if __name__ == "__main__":
    print("=== PRUEBA BUILDER ===")
    director = DirectorHospital()
    builder = HistoriaBuilder()
    director.set_builder(builder)
    director.construir_historia_completa()
    historia_final = builder.get_resultado()
    historia_final.mostrar_historia()

    print("\n=== PRUEBA TEMPLATE METHOD ===")
    inf_cardio = InformeCardiologia()
    inf_cardio.generar_informe()

    print("=== PRUEBA OBSERVER ===")
    paciente = SujetoPaciente()
    medico = MedicoTratante()
    laboratorio = ModuloLaboratorio()
    paciente.adjuntar(medico)
    paciente.adjuntar(laboratorio)
    paciente.set_estado("CRÍTICO")

    print("\n=== PRUEBA PROXY ===")
    proxy = ProxyHistoriaPremium()
    proxy.acceder_historia("Juan Almendariz", "Free")     # Debe denegar
    proxy.acceder_historia("Juan Almendariz", "Premium")  # Debe conceder