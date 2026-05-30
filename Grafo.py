from Arista import Arista
from Nodo import Nodo
import time

class Grafo():

    def __init__(self):

        self.Nodos = {}
        self.Aristas = {}


    def agregar_nodo(self, nombre_nodo):

        if(type(nombre_nodo) == Nodo):
            if self.Nodos.get(nombre_nodo.etiqueta) is None:
                self.Nodos[nombre_nodo.etiqueta] = nombre_nodo

        elif (type(nombre_nodo) == str):
            if self.Nodos.get(nombre_nodo) is None:
                self.Nodos[nombre_nodo] = Nodo(nombre_nodo)
        
    def agregar_arista(self,nombre,nodo_origen,nodo_destino,peso=1):

        if self.Nodos.get(nodo_origen) is None:
            self.agregar_nodo(nodo_origen)

        if self.Nodos.get(nodo_destino) is None:
            self.agregar_nodo(nodo_destino)

        self.Aristas[nombre] = Arista(nodo_origen,nodo_destino,nombre,peso=peso)

    def eliminar_arista(self,nombre):
        self.Aristas.pop(nombre)


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
    
    def toGraphviz(self,algoritmo="",x = 0, y = 0, texto_archivo=False, impresion_peso = False):
        texto = 'digraph X {\n'

        if impresion_peso:
            for nodo in self.Nodos.values():
                texto += f'{nodo.etiqueta}[label="{nodo.etiqueta}({nodo.attributos["peso_acumulado"]})"];\n'

        for arista in self.Aristas:
            texto += f"{self.Aristas[arista].Nodo_origen} -> {str(self.Aristas[arista].Nodo_destino)}"
            if(impresion_peso):
                texto += " [weight=" + str(self.Aristas[arista].attributos["peso"]) + "]"
            texto += ';\n'
        

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
            return Grafo()
        
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

    
    def DFS(self, s, modo=True):

        grafo_dfs = Grafo()
        nodos_descubiertos = {}

        if(self.Nodos.values == None or not self.Nodos.get(s)):
            return None
        
        if modo:
            self.DFS_R(grafo_dfs,s,nodos_descubiertos)
        else:
            self.DFS_I(grafo_dfs,s,nodos_descubiertos)
        
        return grafo_dfs
    
    def Dijkstra(self, s):
        grafo_dijkstra = Grafo()
        nodos_restantes = []

        suma_pesos = 0

        for arista in self.Aristas.values():
            suma_pesos += arista.attributos["peso"]

        print(suma_pesos)

        for nodo in self.Nodos.values():
            nodo.attributos["peso_acumulado"] = suma_pesos

        self.Nodos[s].attributos["peso_acumulado"] = 0

        for nodo in self.Nodos.values():
            nodos_restantes.append(nodo)

        nodos_restantes.sort(key=lambda nodo: nodo.attributos['peso_acumulado'],reverse=True)

        while len(nodos_restantes) > 0:

            nodo_salido = nodos_restantes[len(nodos_restantes)-1]

            nodos_restantes.pop()

            grafo_dijkstra.agregar_nodo(nodo_salido)
            grafo_dijkstra.Nodos[nodo_salido.etiqueta].attributos['peso_acumulado'] = nodo_salido.attributos['peso_acumulado']

            aristas_del_nodo = [arista for arista in self.Aristas.values() if arista.Nodo_origen == nodo_salido.etiqueta]

            
            for arista in aristas_del_nodo:
                if grafo_dijkstra.Nodos.get(arista.Nodo_destino) is None:
                    
                    destino = self.Nodos.get(arista.Nodo_destino)

                    nuevo_peso = nodo_salido.attributos["peso_acumulado"] + arista.attributos["peso"]

                    if nuevo_peso < destino.attributos["peso_acumulado"]:

                        destino.attributos["peso_acumulado"] = nuevo_peso
                        destino.attributos["nodo_padre"] = nodo_salido.etiqueta

                        for nodo in nodos_restantes:

                            if nodo.etiqueta == arista.Nodo_destino:
                                nodo.attributos["peso_acumulado"] = nuevo_peso
                                break 

                    for nodo in nodos_restantes:
                        if(nodo.etiqueta == arista.Nodo_destino):
                            nodo.attributos["peso_acumulado"] = self.Nodos.get(arista.Nodo_destino).attributos.get("peso_acumulado")
                            break

            nodos_restantes.sort(key=lambda nodo: nodo.attributos['peso_acumulado'],reverse=True)

            

        for nodo in self.Nodos.values():

            padre = nodo.attributos["nodo_padre"]

            if padre is not None:

                for arista in self.Aristas.values():

                    if arista.Nodo_origen == padre and arista.Nodo_destino == nodo.etiqueta:
                        grafo_dijkstra.agregar_arista(str(arista.Nodo_origen) + " - " + str(arista.Nodo_destino), arista.Nodo_origen,arista.Nodo_destino,arista.attributos.get("peso"))
                        break

        return grafo_dijkstra
        
    def KruskalD(self):
        Grafo_Kruskal = Grafo()

        aristas_restantes = [arista for arista in self.Aristas.values()]

        aristas_restantes.sort(key=lambda arista: arista.attributos['peso'],reverse=True)

        while len(aristas_restantes) > 0:
            arista = aristas_restantes.pop()           

            Grafo_BFS = Grafo_Kruskal.BFS(arista.Nodo_origen)

            if Grafo_BFS.Nodos.get(arista.Nodo_destino) is None:
                Grafo_Kruskal.agregar_arista(str(arista.Nodo_origen) + " - " + str(arista.Nodo_destino), arista.Nodo_origen,arista.Nodo_destino,arista.attributos.get("peso"))

        return Grafo_Kruskal
    
    def KruskalI(self):
        Grafo_Kruskal = Grafo()
        Grafo_Kruskal.Nodos = self.Nodos.copy()
        Grafo_Kruskal.Aristas = self.Aristas.copy()
        cantidad_de_nodos = len(Grafo_Kruskal.Nodos)
        
        aristas_restantes = [arista for arista in self.Aristas.values()]

        aristas_restantes.sort(key=lambda arista: arista.attributos['peso'],reverse=False)

        while len(aristas_restantes) > 0:

            arista = aristas_restantes.pop()

            Grafo_Kruskal.eliminar_arista(arista.etiqueta)
            if cantidad_de_nodos != len(Grafo_Kruskal.DFS(arista.Nodo_destino).Nodos):
                Grafo_Kruskal.agregar_arista(arista.etiqueta,arista.Nodo_origen,arista.Nodo_destino,arista.attributos["peso"])

        return Grafo_Kruskal
        
    def Prim(self,s):
        Grafo_Prim = Grafo()

        nodos_descubiertos = {}
        nodos_descubiertos[s] = s

        aristas_por_descubrir = [arista for arista in self.Aristas.values() if arista.Nodo_origen == s or arista.Nodo_destino == s]

        while len(aristas_por_descubrir) > 0:

            aristas_por_descubrir.sort(key=lambda arista: arista.attributos['peso'],reverse=True)
            arista = aristas_por_descubrir.pop()

            if nodos_descubiertos.get(arista.Nodo_origen) is None or nodos_descubiertos.get(arista.Nodo_destino) is None:
                nodos_descubiertos[arista.Nodo_origen] = arista.Nodo_origen
                nodos_descubiertos[arista.Nodo_destino] = arista.Nodo_destino

                Grafo_Prim.agregar_arista(arista.etiqueta, arista.Nodo_origen,arista.Nodo_destino,arista.attributos["peso"])

                lista_1 = [arista_p for arista_p in self.Aristas.values() if arista_p.Nodo_origen == arista.Nodo_origen or arista_p.Nodo_destino == arista.Nodo_origen]
                lista_2 = [arista_p for arista_p in self.Aristas.values() if arista_p.Nodo_origen == arista.Nodo_destino or arista_p.Nodo_destino == arista.Nodo_destino]
                
                for arista in lista_1 + lista_2:
                    if not any(x.etiqueta == arista.etiqueta for x in aristas_por_descubrir):
                        aristas_por_descubrir.append(arista)

        return Grafo_Prim



            

            
                


        
        
        
