from .razon import Razon
from cliente.cliente import Cliente
from evento import Evento


class RazonTransferenciaEnviada(Razon):

    def resolver(cliente: Cliente, evento: Evento):
        if cliente.tiene_cuenta_corriente():
            if (evento.monto > (evento.saldoEnCuenta + 10000)):
                return "El monto de la transferencia excede el descubierto"
        elif (evento.monto > evento.saldoEnCuenta):
            return "El monto de la trasnferencia excede el saldo de cuenta"

        if (evento.monto + (evento.monto * cliente.comision_transferencia) > evento.saldoEnCuenta):
            return "El cliente no tiene saldo en cuenta suficiente para pagar la comision de la transferencia"

        return "No se encontro la razon por la cual fue rechazada la transferencia"
