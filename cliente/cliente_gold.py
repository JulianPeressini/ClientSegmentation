from .cliente import Cliente

class ClienteGold(Cliente):

    def __init__(self, datos):
        super(ClienteGold, self).__init__(datos)
        self.limite_transferencia_recibida = 500000
        self.comision_transferencia = 0.05
        self.total_chequeras = 1
        self.total_tarjetas_credito = 1        
    
    def puede_crear_chequera(self):
        return True

    def puede_crear_tarjeta_credito(self):
        return True

    def puede_comprar_dolar(self):
        return True

    def tiene_cuenta_corriente(self):
        return True