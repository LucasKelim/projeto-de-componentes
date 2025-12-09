from entrega_expressa import EntregaExpressa
from entrega_barata import EntregaBarata

ex = EntregaExpressa("Brazil", 200)
eb = EntregaBarata("Brazil", 200)

print("Entrega Expressa:")
print(ex.getDestino())
print(ex.calculaValor())

print("\nEntrega Barata:")
print(eb.getDestino())
print(eb.calculaValor())