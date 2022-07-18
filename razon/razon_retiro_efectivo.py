from .razon import Razon
from cliente.cliente import Cliente
from evento import Evento


class RazonRetiroEfectivo(Razon):

    def resolver(cliente: Cliente, evento: Evento):
        if (evento.monto > evento.cupoDiarioRestante):
            return "El monto a retirar excede el cupo diario restante"

        if cliente.tiene_cuenta_corriente():
            if (evento.monto > (evento.saldoEnCuenta + 10000)):
                return "El monto a retirar excede el descubierto"
        elif (evento.monto > evento.saldoEnCuenta):
            return "El monto a retirar excede el saldo de la cuenta"

        return "No se encontro la razon por la cual fue rechazada la extraccion"
