from Arista import Arista
from Nodo import Nodo

class Grafo():

    def __init__(self):

        self.Nodos = {}
        self.Aristas = {}


    def agregar_nodo(self, nombre_nodo):
        if self.Nodos.get(nombre_nodo) is None:
            self.Nodos[nombre_nodo] = Nodo(nombre_nodo)
        
    def agregar_arista(self,nombre,nodo_origen,nodo_destino):

        if self.Nodos.get(nodo_origen) is None:
            self.agregar_nodo(nodo_origen)

        if self.Nodos.get(nodo_destino) is None:
            self.agregar_nodo(nodo_destino)

        self.Aristas[nombre] = Arista(nodo_origen,nodo_destino,nombre)


    def getGrado(self,nodo):
      grado = 0
      for arista in self.Aristas:
        if self.Aristas[arista].Nodo_origen == nodo or self.Aristas[arista].Nodo_destino == nodo:
          grado += 1
      return grado

    def __str__(self):

        grafo_text = 'Nodos: '
        for nodo in self.Nodos:
            grafo_text += str(nodo) + ', '

        grafo_text += '\nAristas: '

        for arista in self.Aristas:
            grafo_text += str(arista) + ', '

        return grafo_text
    
    def toGraphviz(self,texto_archivo=False,algoritmo="",x = 0, y = 0):
        texto = 'digraph X {\n'

        for arista in self.Aristas:
          texto += str(self.Aristas[arista].Nodo_origen) + ' -> ' + str(self.Aristas[arista].Nodo_destino) + ';\n'

        texto += '}'

        if texto_archivo:
          titulo_archivo = algoritmo + "_" + str(x) + "_" + str(y) + ".gv"
          with open(titulo_archivo, "w") as archivo:
              archivo.write(texto)

        return texto