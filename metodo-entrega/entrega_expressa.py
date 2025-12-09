from entrega import Entrega

class EntregaExpressa(Entrega):
    def __init__(self, destino: str, valorEntrega: float):
        self.__destino = destino
        self.__valorEntrega = valorEntrega
        self.__taxa = 1.3

    def calculaValor(self) -> float:
        """
        Adiciona uma taxa por ser expressa
        """
        valorTotal = self.__valorEntrega * self.__taxa
        return valorTotal
    
    def getDestino(self):
        return self.__destino
    