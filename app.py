from parser import Parser
from procesador_html import Procesadorhtml
from identificador_problemas import IdentificadorProblema

parser = Parser()
cliente, eventos = parser.parseFile("ejemplos_json/eventos_gold.json")
html = Procesadorhtml()
evaluador_transacciones = IdentificadorProblema(cliente)


for e in eventos:
    html.append(evaluador_transacciones.evaluar(e))

html.crear_html(cliente)
