from abc import ABC, abstractmethod

class Pagamento(ABC):

    @abstractmethod
    def processarPagamento(self) -> bool:
        pass

    @abstractmethod
    def getNome(self) -> str:
        pass

    @abstractmethod
    def getDescricao(self) -> str:
        pass