from .cliente import Cliente

class ClienteClassic(Cliente):

    def __init__(self, datos):
        super(ClienteClassic, self).__init__(datos)