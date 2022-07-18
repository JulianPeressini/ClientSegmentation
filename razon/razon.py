from abc import ABC, abstractmethod
from cliente.cliente import Cliente
from evento import Evento


class Razon(ABC):

    @abstractmethod
    def resolver(self, cliente: Cliente, evento: Evento) -> str:
        pass
