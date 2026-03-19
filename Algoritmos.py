from Arista import Arista
from Nodo import Nodo
from Grafo import Grafo

import math
import random

class Algoritmos():

  def randomarray(self, size):
    array = []
    for i in range(size):
      array.append(i)

    for i in range(size):
      j = random.randint(0, size - 1)
      aux = array[i]
      array[i] = array[j]
      array[j] = aux

    return array

  def grafoMalla(self,m, n, diagonal=False, dirigido = False):
    """
    :param m: número de filas
    :param n: número de columnas
    :param diagonal: True si el grafo tiene diagonales
    :param dirigido: el grafo es dirigido?
    """
    grafo = Grafo()

    m = max(2, m)
    n = max(2, n)

    for i in range(m):
      for j in range(n):

        nodo_actual = i * m + j
        str_nodo_actual = str(nodo_actual)

        if j < n - 1:
          proximo_nodo = nodo_actual + 1
          grafo.agregar_arista(str_nodo_actual + " - " + str(proximo_nodo), str_nodo_actual, str(proximo_nodo))
        
        if i < m - 1:
          proximo_nodo = nodo_actual + m
          grafo.agregar_arista(str_nodo_actual + " - " + str(proximo_nodo), str_nodo_actual, str(proximo_nodo))

        if diagonal:
          if j < n - 1 and i < m - 1:
            proximo_nodo = nodo_actual + m + 1
            grafo.agregar_arista(str_nodo_actual + " - " + str(proximo_nodo), str_nodo_actual, str(proximo_nodo))
          
          if j - 1 >= 0 and i < m - 1:
            proximo_nodo = nodo_actual + m - 1
            grafo.agregar_arista(str_nodo_actual + " - " + str(proximo_nodo), str_nodo_actual, str(proximo_nodo))

    return grafo

  def grafoErdosRenyi(self, n, m, dirigido=False):
    """
    Genera grafo aleatorio con el modelo Erdos-Renyi
    :param n: número de nodos (> 0)
    :param m: número de aristas (>= n-1)
    :param dirigido: el grafo es dirigido?
    :return: grafo generado
    """

    grafo = Grafo()

    for i in range(n):
      grafo.agregar_nodo(str(i))

    for i in range(m):
      nodo_origen = str(random.randint(0, n - 1))
      nodo_destino = str(random.randint(0, n - 1))

      if nodo_origen != nodo_destino:
        grafo.agregar_arista(nodo_origen + " - " + nodo_destino, nodo_origen, nodo_destino)

    return grafo

  def grafoGilbert(self, n, p, dirigido=False):
    """
    Genera grafo aleatorio con el modelo Gilbert
    :param n: número de nodos (> 0)
    :param p: probabilidad de crear una arista (0, 1)
    :param dirigido: el grafo es dirigido?
    :return: grafo generado
    """

    grafo = Grafo()

    for i in range(n):
      grafo.agregar_nodo(str(i))

    for i in range(n):
      for j in range(n):
        if random.random() < p:
          if i != j:
            grafo.agregar_arista(str(i) + " - " + str(j), str(i), str(j))

    return grafo

  def grafoGeografico(self, n, r, dirigido=False):
      """
      Genera grafo aleatorio con el modelo geográfico simple
      :param n: número de nodos (> 0)
      :param r: distancia máxima para crear un nodo (0, 1)
      :param dirigido: el grafo es dirigido?
      :return: grafo generado
      """

      grafo = Grafo()

      for i in range(n):
        grafo.agregar_nodo(str(i))
        grafo.Nodos[str(i)].attributos['coordenada_X'] = random.random()
        grafo.Nodos[str(i)].attributos['coordenada_Y'] = random.random()

      for i in range(n):
        for j in range(i,n):
          if(i != j):
            x1, y1 = grafo.Nodos[str(i)].attributos['coordenada_X'], grafo.Nodos[str(i)].attributos['coordenada_Y']
            x2, y2 = grafo.Nodos[str(j)].attributos['coordenada_X'], grafo.Nodos[str(j)].attributos['coordenada_Y']

            distancia = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

            if distancia <= r:
              grafo.agregar_arista(str(i) + " - " + str(j), str(i), str(j))

      return grafo

  def grafoBarabasiAlbert(self, n, d, dirigido=False):
    """
    Genera grafo aleatorio con el modelo Barabasi-Albert
    :param n: número de nodos (> 0)
    :param d: grado máximo esperado por cada nodo (> 1)
    :param dirigido: el grafo es dirigido?
    :return: grafo generado
    """

    grafo = Grafo()

    """
    arreglo_aleatorio = []
    for i in range(n):
      arreglo_aleatorio.append(i)
    """

    for i in range(n):
      grafo.agregar_nodo(str(i))

    for i in range(1,n):
      arreglo_aleatorio = self.randomarray(n)

      for j in range(n):
        grado_nodo_actual = grafo.getGrado(str(i))
        if grado_nodo_actual < d:
          grado = grafo.getGrado(str(arreglo_aleatorio[j]))
          probabilidad = 1 - grado / d

          if random.random() < probabilidad:
            if arreglo_aleatorio[j] != i:
              grafo.agregar_arista(str(i) + " - " + str(arreglo_aleatorio[j]), str(i), str(arreglo_aleatorio[j]))

    return grafo


  def grafoDorogovtsevMendes(self, n, dirigido=False):
    """
    Genera grafo aleatorio con el modelo Barabasi-Albert
    :param n: número de nodos (≥ 3)
    :param dirigido: el grafo es dirigido?
    :return: grafo generado
    """


    grafo = Grafo()

    grafo.agregar_arista(str(0) + " - " + str(1), str(0), str(1))
    grafo.agregar_arista(str(0) + " - " + str(2), str(0), str(2))
    grafo.agregar_arista(str(1) + " - " + str(2), str(1), str(2))

    for i in range(3,n):
      grafo.agregar_nodo(str(i))

      arreglo_aleatorio = self.randomarray(i)

      arista_elegida = list(grafo.Aristas.values())[arreglo_aleatorio[0]]

      grafo.agregar_arista(str(i) + " - " + str(arista_elegida.Nodo_origen), str(i), str(arista_elegida.Nodo_origen))
      grafo.agregar_arista(str(i) + " - " + str(arista_elegida.Nodo_destino), str(i), str(arista_elegida.Nodo_destino))

    return grafo