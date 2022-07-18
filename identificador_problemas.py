from cliente.cliente import Cliente
from evento import Evento
from razon.razon_alta_chequera import RazonAltaChequera
from razon.razon_alta_tarjeta_credito import RazonAltaTarjetaCredito
from razon.razon_compra_dolar import RazonCompraDolar
from razon.razon_retiro_efectivo import RazonRetiroEfectivo
from razon.razon_transferencia_enviada import RazonTransferenciaEnviada
from razon.razon_transferencia_recibida import RazonTransferenciaRecibida


class IdentificadorProblema():

    def __init__(self, cliente: Cliente,):
        self.cliente = cliente

    def evaluar(self, evento: Evento):

        if (evento.estado == "ACEPTADA"):
            self.razon = "-"

        elif (evento.tipo == "ALTA_CHEQUERA"):
            self.razon = RazonAltaChequera.resolver(self.cliente, evento)

        elif (evento.tipo == "ALTA_TARJETA_CREDITO"):
            self.razon = RazonAltaTarjetaCredito.resolver(
                self.cliente, evento)

        elif (evento.tipo == "COMPRA_DOLAR"):
            self.razon = RazonCompraDolar.resolver(self.cliente, evento)

        elif (evento.tipo == "RETIRO_EFECTIVO_CAJERO_AUTOMATICO"):
            self.razon = RazonRetiroEfectivo.resolver(
                self.cliente, evento)

        elif (evento.tipo == "TRANSFERENCIA_ENVIADA"):
            self.razon = RazonTransferenciaEnviada.resolver(
                self.cliente, evento)

        elif (evento.tipo == "TRANSFERENCIA_RECIBIDA"):
            self.razon = RazonTransferenciaRecibida.resolver(
                self.cliente, evento)

        evento.setRazon(self.razon)

        return evento
