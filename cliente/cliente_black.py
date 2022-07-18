from .cliente import Cliente

class ClienteBlack(Cliente):


    def __init__(self, datos):
        super(ClienteBlack, self).__init__(datos)
        self.total_chequeras = 2
        self.comision_transferencia = 0
        self.total_tarjetas_credito = 5

    def puede_crear_chequera(self):
        return True

    def puede_crear_tarjeta_credito(self):
        return True

    def puede_comprar_dolar(self):
        return True

    def tiene_cuenta_corriente(self):
        return True

    def necesita_autorizar_transferencia_recibida(self):
        return False

    def tiene_limite_transferencia_recibida(self):
        return True