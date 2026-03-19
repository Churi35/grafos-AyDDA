from Algoritmos import Algoritmos

algoritmos = Algoritmos()
x = 50
y = 50
#grafo = algoritmos.grafoDorogovtsevMendes(x)
#grafo = algoritmos.grafoBarabasiAlbert(x, y)
#grafo = algoritmos.grafoGeografico(x, y)
#grafo = algoritmos.grafoGilbert(x, y)
grafo = algoritmos.grafoMalla(x,y,diagonal=True)
#grafo = algoritmos.grafoErdosRenyi(x,y)

print(grafo)

grafo.toGraphviz(True,"Malla",x,y)
