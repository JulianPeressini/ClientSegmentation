from cliente.cliente import Cliente
from cliente.direccion import Direccion
from evento import Evento


class Procesadorhtml:

    def __init__(self):
        self.elementos = []

    def append(self, elemento):
        self.elementos.append(elemento)

    def crear_html(self, cliente: Cliente):
        transacciones = ""
        for e in self.elementos:
            transacciones += "<tr><td>{fecha}</td><td>{tipo}</td><td>{estado}</td><td>{monto}</td><td>{razon}</td></tr>".format(
                fecha=e.fecha,
                tipo=e.tipo.replace("_", " "),
                estado=e.estado,
                monto=e.monto,
                razon=e.razon
            )
        html = """
            <html>
                <title>Listado de transacciones</title>
                <body>
                    <h1>{apellido}, {nombre}</h1>
                    <div>Numero cliente: {numero}</div>
                    <div>DNI: {dni}</div>
                    <div>Direccion: {direccion}</div>
                    <table>
                        <tr><td>Fecha</td><td>Tipo</td><td>Estado</td><td>Monto</td><td>Razon</td></tr>
                        {transacciones}
                    </table>
                </body>
            </html>
        """.format(
            direccion=str(cliente.direccion),
            numero=cliente.numero,
            nombre=cliente.nombre,
            apellido=cliente.apellido,
            dni=cliente.dni,
            transacciones=transacciones
        )

        archivo = open("index.html", "w")
        archivo.write(html)
        archivo.close()
