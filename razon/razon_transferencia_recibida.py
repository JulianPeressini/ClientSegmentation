from .razon import Razon
from cliente.cliente import Cliente
from evento import Evento


class RazonTransferenciaRecibida(Razon):

    def resolver(cliente: Cliente, evento: Evento):
        if cliente.necesita_autorizar_transferencia_recibida():
            if (evento.monto > cliente.limite_transferencia_recibida):
                return "El monto de la transferencia es mayor a la cantidad de dinero que el tipo de cliente puede recibir"

        return "No se pudo encontrar la razon por la cual la transferencia fue rechazada"
