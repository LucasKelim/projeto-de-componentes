import random
from pagamento import Pagamento

class PagamentoPix(Pagamento):
    def __init__(self, valorTotal: float):
        self.__valorTotal = valorTotal

    def processarPagamento(self) -> bool:
        """
        Processa pagamento via Pix

        :return: Retorna um bool se o pagamento via Pix foi precessado
        :rtype: bool
        """
        return random.choice([True, False])
    
    def getDescricao(self):
        return "Pix"
    