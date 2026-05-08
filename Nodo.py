class Nodo():

    def __init__(self,etiqueta=""):
        self.etiqueta = etiqueta
        self.attributos = {
            'coordenada_X':0,
            'coordenada_Y':0,
            'peso_acumulado': 0,
            'nodo_padre': None,
        }

    def __str__(self):
        return self.etiqueta
