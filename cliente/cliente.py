from .direccion import Direccion

BLACK = "BLACK"
CLASSIC = "CLASSIC"
GOLD = "GOLD"

class Cliente:

    def __init__(self, datos) -> None:
        self.numero = datos["numero"]
        self.nombre = datos["nombre"]
        self.apellido = datos["apellido"]
        self.dni = datos["dni"]
        self.direccion = Direccion(datos["direccion"])
        self.limite_transferencia_recibida = 150000
        self.comision_transferencia = 0.1
        self.total_chequeras = 0
        self.total_tarjetas_credito = 0
        
    def puede_crear_chequera(self):
        return False
    
    def puede_crear_tarjeta_credito(self):
        return False

    def puede_comprar_dolar(self):
        return False

    def tiene_cuenta_corriente(self):
        return False

    def necesita_autorizar_transferencia_recibida(self):
        return True