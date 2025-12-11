import random
from pagamento import Pagamento
from datetime import date

class PagamentoPix(Pagamento):
    def __init__(self, valorTotal: float, validade: date):
        self.__valorTotal = valorTotal
        self.__validade = validade

    def processarPagamento(self) -> bool:
        """
        Processa pagamento via Pix

        :return: Retorna um bool se o pagamento via Pix foi precessado
        :rtype: bool
        """
        return random.choice([True, False])
    
    def verificarValidade(self):
        return date.today() <= self.__validade
    
    def getNome(self):
        return "Pix"
    
    def getDescricao(self):
        return f"""
            Pagamento via {self.getNome()}
            Preço: R$ {self.__valorTotal:.2f}
            Validade: {self.__validade.strftime("%d/%m/%Y")}
        """
    