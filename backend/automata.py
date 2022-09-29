import graphviz
import json
from operaciones.union import *
from operaciones.reverso import *
from operaciones.interseccion import *
from operaciones.complemento import *


class GraficoAutomata:
    def cargarDatos(self, listaRutas):
        ruta1 = listaRutas[0]
        ruta2 = listaRutas[1]
        with open(ruta1) as contenido:
            datos1 = json.load(contenido)
        self.cargarAutomata1(datos1)
        with open(ruta2) as contenido:
            datos2 = json.load(contenido)
        self.cargarAutomata2(datos2)
        union = Union()
        inters = Interseccion()
        complemento = Complemento()
        reverso = Reverso()
        nombre1 = "unionAutomataUnoYCero.gv"
        interseccion = "Interseccion_AB"
        nombre2 = 'unionAutomataTresUnosyTresCeros.gv'
        nombre3 = 'Union'
        nombre4 = 'Reverso'
        nombre5 = 'Complemento'
        nombre6 = 'Interseccion'
        union.unionAutomata(datos1, datos2, nombre3)
        inters.interseccionAutomata(datos1, datos2, nombre6)
        complemento.complementoAutomata(datos1, nombre5)
        reverso.reversoAutomata(datos1, nombre4)

    def cargarAutomata1(self, diccionario):
        #f = graphviz.Digraph('finite_state_machine', filename='inicie_tres_ceros.gv')
        f = graphviz.Digraph('finite_state_machine',
                             filename='Por_lo_menos_una_A.gv')
        f.attr(rankdir='LR', size='8,5')

        f.attr('node', shape='doublecircle')

        transiciones = diccionario['transiciones']
        estado = diccionario['estados']

        estadoAceptacion = estado["Aceptacion"]
        f.node(estadoAceptacion)
        f.attr('node', shape='circle')
        for i in range(len(transiciones)):
            origen = transiciones[i].get("Origen")
            destino = transiciones[i].get("Destino")
            transicion = transiciones[i].get("transicion")
            f.edge(origen, destino, label=transicion)
        f.save()

    def cargarAutomata2(self, diccionario):
        #j = graphviz.Digraph('finite_state_machine', filename='termine_tres_unos.gv')
        j = graphviz.Digraph('finite_state_machine',
                             filename='Por_lo_menos_una_B.gv')
        j.attr(rankdir='LR', size='8,5')

        j.attr('node', shape='doublecircle')

        transiciones = diccionario['transiciones']
        estado = diccionario['estados']

        estadoAceptacion = estado["Aceptacion"]
        estadoInicial = estado["inicial"]
        j.node(estadoAceptacion)
        j.attr('node', shape='circle')
        for i in range(len(transiciones)):
            origen = transiciones[i].get("Origen")
            destino = transiciones[i].get("Destino")
            transicion = transiciones[i].get("transicion")
            j.edge(origen, destino, label=transicion)
        j.save()


a = GraficoAutomata()
rutas = []
ruta1 = "/home/krozfu/Documents/Automatas/python/project/backend/archivos/Por_lo_menos_un_cero.json"
ruta2 = "/home/krozfu/Documents/Automatas/python/project/backend/archivos/Por_lo_menos_un_unoo.json"
rutas.append(ruta1)
rutas.append(ruta2)

rutas2 = []
ruta3 = "/home/krozfu/Documents/Automatas/python/project/backend/archivos/Inicie_con_tres_ceros.json"
ruta4 = "/home/krozfu/Documents/Automatas/python/project/backend/archivos/Termine_con_tres_unos.json"
rutas2.append(ruta3)
rutas2.append(ruta4)

rutas3 = []
ruta5 = "/home/krozfu/Documents/Automatas/python/project/backend/archivos/Por_lo_menos_una_A.json"
ruta6 = "/home/krozfu/Documents/Automatas/python/project/backend/archivos/Por_lo_menos_una_B.json"
rutas3.append(ruta5)
rutas3.append(ruta6)

a.cargarDatos(rutas2)
