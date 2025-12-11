from pagamento_pix import PagamentoPix
from pagamento_cartao_credito import PagamentoCartaoCredito
from pagamento import Pagamento

pix = PagamentoPix(100)
cartaoCredito = PagamentoCartaoCredito(100, 3)


def realizarPagamento(pagamento: Pagamento):
    print(f"Pagamento {pagamento.getDescricao()}")
    if (pagamento.processarPagamento()):
        print(f"Pagamento via {pagamento.getDescricao()} processado")
    else:
        print(f"Falha ao processar pagamento via {pagamento.getDescricao()}")

print()
realizarPagamento(pix)
print()
print("---------------------------")
print()
realizarPagamento(cartaoCredito)
print()