from cliente.cliente import CLASSIC, GOLD, BLACK
from cliente.cliente_classic import ClienteClassic
from cliente.cliente_gold import ClienteGold
from cliente.cliente_black import ClienteBlack
from evento import Evento
import json


class Parser:

    def parseFile(self, file_name):
        transacciones = []
        with open(file_name) as jsonFile:
            eventos = json.load(jsonFile)
            cliente = self.parsearCliente(eventos)
            for transaccion in eventos["transacciones"]:
                transacciones.append(Evento(transaccion))
        return (cliente, transacciones)

    def parsearCliente(self, datos):
        tipo = datos["tipo"]

        if (tipo == CLASSIC):
            cliente = ClienteClassic(datos)
        elif (tipo == GOLD):
            cliente = ClienteGold(datos)
        elif (tipo == BLACK):
            cliente = ClienteBlack(datos)
        else:
            raise Exception("Tipo de cliente no existente")

        return cliente
