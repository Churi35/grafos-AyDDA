from Algoritmos import Algoritmos
from Grafo import Grafo
from Nodo import Nodo

import sys

# Aumentar el límite a 10,000 (o lo que necesites)
sys.setrecursionlimit(300000)

algoritmos = Algoritmos()
algoritmos_lista = ["Malla","Dorogovtsev","Geografico","Gilbert","Barabasi","Erdos"]
#cantidades = [30,100,500]
cantidades = [30,100]

#grafo = algoritmos.grafoDorogovtsevMendes(x)
#grafo = algoritmos.grafoBarabasiAlbert(x, y)
#grafo = algoritmos.grafoGeografico(x, y)
#grafo = algoritmos.grafoGilbert(x, y)
#grafo = algoritmos.grafoMalla(3,3,diagonal=True)
#grafo.toGraphviz("Malla",3,3, texto_archivo = True, impresion_peso=True)
#grafo = algoritmos.grafoErdosRenyi(x,y)

"""
for x in cantidades:
    for algoritmo in algoritmos_lista:
        if algoritmo == "Malla":
            y = int(x / 10)
            x_1 = int(x / y)
            grafo = algoritmos.grafoMalla(x_1,y,diagonal=False)

        if algoritmo == "Dorogovtsev":
            y = 0
            grafo = algoritmos.grafoDorogovtsevMendes(x)

        if algoritmo == "Geografico":
            y = 0.3
            grafo = algoritmos.grafoGeografico(x, y)

        if algoritmo == "Gilbert":
            y = 0.3
            grafo = algoritmos.grafoGilbert(x, y)
        
        if algoritmo == "Barabasi":
            y = int(x*.1)
            grafo = algoritmos.grafoBarabasiAlbert(x, y)

        if algoritmo == "Erdos":
            y = int(x*1.5)
            grafo = algoritmos.grafoErdosRenyi(x, y)

        grafo.toGraphviz(True,algoritmo,x,y)

        print(algoritmo+"_bfs")
        grafo_bfs = grafo.BFS("0")
        grafo_bfs.toGraphviz(True,algoritmo+"_bfs",x,y)

        print(algoritmo+"_dfs_r")
        grafo_dfs_r = grafo.DFS("0",True)
        grafo_dfs_r.toGraphviz(True,algoritmo+"_dfs_r",x,y)

        print(algoritmo+"_dfs_i")
        grafo_dfs_i = grafo.DFS("0",True)
        grafo_dfs_i.toGraphviz(True,algoritmo+"_dfs_i",x,y)

"""
"""
grafo = algoritmos.grafoMalla(x,y,diagonal=False)
print(grafo)
grafo.toGraphviz(True,"Malla",x,y)

grafo_bfs = grafo.BFS("0")
print(grafo_bfs)

grafo_dfs_r = grafo.DFS("0",True)
print(grafo_dfs_r)
grafo_dfs_r.toGraphviz(True,"Malla_dfs_r",x,y)

grafo_dfs_i = grafo.DFS("0",True)
print(grafo_dfs_i)
grafo_dfs_i.toGraphviz(True,"Malla_dfs_i",x,y)
*/

"""


"""
for x in cantidades:
    for algoritmo in algoritmos_lista:
        if algoritmo == "Malla":
            y = int(x / 10)
            x_1 = int(x / y)
            grafo = algoritmos.grafoMalla(x_1,y,diagonal=False)

        if algoritmo == "Dorogovtsev":
            y = 0
            grafo = algoritmos.grafoDorogovtsevMendes(x)

        if algoritmo == "Geografico":
            y = 0.3
            grafo = algoritmos.grafoGeografico(x, y)

        if algoritmo == "Gilbert":
            y = 0.3
            grafo = algoritmos.grafoGilbert(x, y)
        
        if algoritmo == "Barabasi":
            y = int(x*.1)
            grafo = algoritmos.grafoBarabasiAlbert(x, y)

        if algoritmo == "Erdos":
            y = int(x*1.5)
            grafo = algoritmos.grafoErdosRenyi(x, y)

        grafo.toGraphviz(algoritmo,x,y,True,True)

        print(algoritmo+"_dijkstra")
        grafo_dijkstra = grafo.Dijkstra('0')
        grafo_dijkstra.toGraphviz(algoritmo+"_dijkstra",x,y,True,True)

"""

"""
for x in cantidades:
    for algoritmo in algoritmos_lista:
        if algoritmo == "Malla":
            y = int(x / 10)
            x_1 = int(x / y)
            grafo = algoritmos.grafoMalla(x_1,y,diagonal=False)

        if algoritmo == "Dorogovtsev":
            y = 0
            grafo = algoritmos.grafoDorogovtsevMendes(x)

        if algoritmo == "Geografico":
            y = 0.3
            grafo = algoritmos.grafoGeografico(x, y)

        if algoritmo == "Gilbert":
            y = 0.3
            grafo = algoritmos.grafoGilbert(x, y)
        
        if algoritmo == "Barabasi":
            y = int(x*.1)
            grafo = algoritmos.grafoBarabasiAlbert(x, y)

        if algoritmo == "Erdos":
            y = int(x*1.5)
            grafo = algoritmos.grafoErdosRenyi(x, y)

        grafo.toGraphviz(algoritmo,x,y,True,True)

        grafo_kruskal_direc = grafo.KruskalD()
        grafo_kruskal_direc.toGraphviz(algoritmo+"_kruskal_d",3,3,True,True)

"""

for x in cantidades:
    for algoritmo in algoritmos_lista:
        if algoritmo == "Malla":
            y = int(x / 10)
            x_1 = int(x / y)
            grafo = algoritmos.grafoMalla(x_1,y,diagonal=False)

        if algoritmo == "Dorogovtsev":
            y = 0
            grafo = algoritmos.grafoDorogovtsevMendes(x)

        if algoritmo == "Geografico":
            y = 0.3
            grafo = algoritmos.grafoGeografico(x, y)

        if algoritmo == "Gilbert":
            y = 0.3
            grafo = algoritmos.grafoGilbert(x, y)
        
        if algoritmo == "Barabasi":
            y = int(x*.1)
            grafo = algoritmos.grafoBarabasiAlbert(x, y)

        if algoritmo == "Erdos":
            y = int(x*1.5)
            grafo = algoritmos.grafoErdosRenyi(x, y)

        grafo.toGraphviz(algoritmo,x,y,True,True)

        grafo_kruskal_direc = grafo.KruskalD()
        grafo_kruskal_direc.toGraphviz(algoritmo+"_kruskal_d",x,y,True,True)

        grafo_kruskal_inverso = grafo.KruskalI()
        grafo_kruskal_inverso.toGraphviz(algoritmo+"_kruskal_i",x,y,True,True)

        grafo_prim = grafo.Prim("0")
        grafo_prim.toGraphviz(algoritmo + "_prim",x,y,True,True)


