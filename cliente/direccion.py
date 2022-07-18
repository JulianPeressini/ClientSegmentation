class Direccion:

    def __init__(self, datos_direccion):
        self.calle = datos_direccion["calle"]
        self.numero = datos_direccion["numero"]
        self.ciudad = datos_direccion["ciudad"]
        self.provincia = datos_direccion["provincia"]
        self.pais = datos_direccion["pais"]

    def __str__(self):
        return f'{self.calle} {self.numero}, {self.ciudad}. {self.provincia}, {self.pais}.'
