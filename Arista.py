class Arista():

    def __init__(self,Nodo_origen, Nodo_destino, etiqueta=""):
        self.etiqueta = etiqueta
        self.Nodo_origen = Nodo_origen
        self.Nodo_destino = Nodo_destino

    def __str__(self):
        
        return "(" + self.Nodo_origen+ "," + self.Nodo_destino + "," + str(self.etiqueta)+ ")"
