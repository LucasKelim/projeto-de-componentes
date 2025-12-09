from abc import ABC, abstractmethod

class Entrega(ABC):

    @abstractmethod
    def calculaValor(self) -> float:
        """
        Descrição de calculaValor
        
        :return: Calcula o valor da entrega
        :rtype: float
        """
        pass

    @abstractmethod
    def getDestino(self) -> str:
        pass