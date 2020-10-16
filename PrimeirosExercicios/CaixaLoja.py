print("Lojas tabajara")
ValorTotal = 0
AdicionaProduto = None
ProdutoEntrada = 0
while AdicionaProduto != 0:
    ProdutoEntrada += 1
    AdicionaProduto = float(input(f"Produto {ProdutoEntrada}: R$ "))
    ValorTotal = ValorTotal + AdicionaProduto 
print("Total: R$ %.2f" % ValorTotal )
ValorPago = float(input("Dinheiro: R$ "))
print(f"Troco: R$ {ValorPago - ValorTotal}")