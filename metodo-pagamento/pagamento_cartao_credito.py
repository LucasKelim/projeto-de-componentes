import random
from pagamento import Pagamento

class PagamentoCartaoCredito(Pagamento):
    def __init__(self, valorTotal: float, parcelas: int):
        self.__valorTotal = valorTotal
        self.__parcelas = parcelas

    def processarPagamento(self) -> bool:
        """
        Processa pagamento via Cartão de Crédito

        :return: Retorna um bool se o pagamento via Cartão de Crédito foi precessado
        :rtype: bool
        """
        return random.choice([True, False])
    
    def valorParcela(self) -> float:
        return self.__valorTotal / self.__parcelas
    
    def getNome(self):
        return "Cartão de Crédito"

    def getDescricao(self):
        return f"""
            Pagamento via {self.getNome()}
            Preço Total: R$ {self.__valorTotal:.2f}
            Parcelas: {self.__parcelas}
            Preço da Parcela: R$ {self.valorParcela():.2f}
        """
