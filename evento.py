class Evento:

    def __init__(self, datos_transaccion):
        self.estado = datos_transaccion["estado"]
        self.tipo = datos_transaccion["tipo"]
        self.cuentaNumero = datos_transaccion["cuentaNumero"]
        self.cupoDiarioRestante = datos_transaccion["cupoDiarioRestante"]
        self.monto = datos_transaccion["monto"]
        self.fecha = datos_transaccion["fecha"]
        self.numero = datos_transaccion["numero"]
        self.saldoEnCuenta = datos_transaccion["saldoEnCuenta"]
        self.totalTarjetasDeCreditoActualmente = datos_transaccion[
            "totalTarjetasDeCreditoActualmente"]
        self.totalChequerasActualmente = datos_transaccion["totalChequerasActualmente"]
        self.razon = ""

    def setRazon(self, razon):
        self.razon = razon
