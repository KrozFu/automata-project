import graphviz
import json


class GraficoAutomata:
    def __init__(self):
        pass

    def cargarDatos(self, ruta):
        with open(ruta) as contenido:
            datos = json.load(contenido)
        return self.cargar(datos)

    def cargar(self, diccionario):
        f = graphviz.Digraph('finite_state_machine', filename='automata.gv')
        f.attr(rankdir='LR', size='8,5')
        f.attr('node', shape='doublecircle')
        f.node(diccionario["estados"].get("Aceptacion"))
        f.attr('node', shape='circle')

        li = diccionario["transiciones"]
        dicci = dict(zip(range(len(li)), li))

        for c, v in dicci.items():
            f.edge(v.get("Origen"), v.get("Destino"),
                   label=str(v.get("transicion")))
        au = f
        return str(au)


# a = GraficoAutomata()
# grafo = a.cargarDatos("Inicie_con_tres_ceros.json")
# print(type(grafo))
# print(grafo)
