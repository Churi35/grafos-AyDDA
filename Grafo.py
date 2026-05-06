from Arista import Arista
from Nodo import Nodo
import time

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
    
    def BFS(self, s):
       
        grafo_bfs = Grafo()
        capas = []
        nodos_descubiertos = {}

        if(self.Nodos.values == None or not self.Nodos.get(s)):
            return None
        
        grafo_bfs.agregar_nodo(s)
        nodos_descubiertos[s] = s
        capas.append({s: s})

        i = 0

        while i < len(capas):
          
            siguiente_capa = {}

            for nodo in capas[i].values():
                aristas_del_nodo = [arista for arista in self.Aristas.values() if arista.Nodo_origen == nodo or arista.Nodo_destino == nodo]

                for arista in aristas_del_nodo:

                    if arista.Nodo_origen == nodo:
                        siguiente_nodo = arista.Nodo_destino
                    else:
                        siguiente_nodo = arista.Nodo_origen

                    if not nodos_descubiertos.get(siguiente_nodo):
                        grafo_bfs.agregar_arista(nodo + " - " + siguiente_nodo, nodo, siguiente_nodo)
                        siguiente_capa[siguiente_nodo] = nodos_descubiertos[siguiente_nodo] = siguiente_nodo
            
            if siguiente_capa:
                capas.append(siguiente_capa)
            
            i += 1
        
        return grafo_bfs
    
    def DFS_R(self, grafo_dfs,nodo_base , nodos_descubiertos):
        grafo_dfs.agregar_nodo(nodo_base)
        nodos_descubiertos[nodo_base] = nodo_base

        aristas_del_nodo = [arista for arista in self.Aristas.values() if arista.Nodo_origen == nodo_base or arista.Nodo_destino == nodo_base]

        for arista in aristas_del_nodo:
            if arista.Nodo_origen == nodo_base:
                siguiente_nodo = arista.Nodo_destino
            else:
                siguiente_nodo = arista.Nodo_origen

            if not nodos_descubiertos.get(siguiente_nodo):
                grafo_dfs.agregar_arista(nodo_base + " - " + siguiente_nodo, nodo_base, siguiente_nodo)
                self.DFS_R(grafo_dfs,siguiente_nodo,nodos_descubiertos)

    def DFS_I(self, grafo_dfs,nodo_base , nodos_descubiertos):
        pila = []
        condicion_pila = True

        pila.append(nodo_base)
        nodos_descubiertos[nodo_base] = nodo_base

        grafo_dfs.agregar_nodo(nodo_base)

        while len(pila) > 0:
            condicion_pila = True
            nodo_actual = pila[len(pila)-1]
            nodos_descubiertos[nodo_actual] = nodo_actual

            aristas_del_nodo = [arista for arista in self.Aristas.values() if arista.Nodo_origen == nodo_actual or arista.Nodo_destino == nodo_actual]

            print(pila)

            for arista in aristas_del_nodo:
                if arista.Nodo_origen == nodo_actual:
                    siguiente_nodo = arista.Nodo_destino
                else:
                    siguiente_nodo = arista.Nodo_origen

                if not nodos_descubiertos.get(siguiente_nodo):
                    grafo_dfs.agregar_arista(nodo_actual + " - " + siguiente_nodo, nodo_actual, siguiente_nodo)
                    pila.append(siguiente_nodo)
                    condicion_pila = False
                    break
                
            if condicion_pila:
                pila.pop()

    
    def DFS(self, s, modo):

        grafo_dfs = Grafo()
        nodos_descubiertos = {}

        if(self.Nodos.values == None or not self.Nodos.get(s)):
            return None
        
        if modo:
            self.DFS_R(grafo_dfs,s,nodos_descubiertos)
        else:
            self.DFS_I(grafo_dfs,s,nodos_descubiertos)
        
        return grafo_dfs

    


        
             


       
       
       
