from .razon import Razon
from cliente.cliente import Cliente
from evento import Evento


class RazonAltaChequera(Razon):

    def resolver(cliente: Cliente, evento: Evento):
        if not cliente.puede_crear_chequera():
            return "El cliente no puede tener chequeras"

        if (evento.totalChequerasActualmente + 1 > cliente.total_chequeras):
            return "Ya se tiene el cupo de chequeras disponibles"

        return "No se pudo determinar la razon por la cual no se creo la chequera"
