from entrega import Entrega

class EntregaBarata(Entrega):
    def __init__(self, destino: str, valorEntrega: float):
        self.__destino = destino
        self.__valorEntrega = valorEntrega

    def calculaValor(self):
        return self.__valorEntrega
    
    def getDestino(self):
        return self.__destino

    