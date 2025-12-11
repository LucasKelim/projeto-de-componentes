from pagamento_pix import PagamentoPix
from pagamento_cartao_credito import PagamentoCartaoCredito
from pagamento import Pagamento
from datetime import date

pix = PagamentoPix(100, date(2025, 12, 11))
cartaoCredito = PagamentoCartaoCredito(100, 3)

def realizarPagamento(pagamento: Pagamento):
    print(f"Pagamento {pagamento.getNome()}")
    if (pagamento.processarPagamento()):
        print(pagamento.getDescricao())
    else:
        print(f"Falha ao processar pagamento via {pagamento.getNome()}")

print()
realizarPagamento(pix)
print()
print("---------------------------")
print()
realizarPagamento(cartaoCredito)
print()