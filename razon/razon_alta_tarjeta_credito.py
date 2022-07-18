from .razon import Razon
from cliente.cliente import Cliente
from evento import Evento


class RazonAltaTarjetaCredito(Razon):

    def resolver(cliente: Cliente, evento: Evento):
        if not cliente.puede_crear_tarjeta_credito():
            return "El cliente no puede tener tarjetas de credito"

        if (evento.totalTarjetasDeCreditoActualmente + 1 > cliente.total_tarjetas_credito):
            return "Ya se tiene el cupo de tarjetas de credito disponibles"

        return "No se pudo determinar la razon por la cual no se creo la tarjeta de credito"
