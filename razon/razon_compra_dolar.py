from .razon import Razon
from cliente.cliente import Cliente
from evento import Evento


class RazonCompraDolar(Razon):

    def resolver(cliente: Cliente, evento: Evento):
        if not cliente.puede_comprar_dolar():
            return "Este tipo de cuentas no puede comprar dolares"

        if evento.monto > evento.saldoEnCuenta:
            return "No tiene saldo suficiente para comprar los dolares"

        return "No se pudo determinar la razon por la cual no se pudo comprar dolares"
