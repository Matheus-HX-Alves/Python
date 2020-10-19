valorPrestacao = None
valorTotal  = 0

def valorPagamento(valorPrestacao,diasAtrasos):
    if diasAtrasos > 0:
        totalPrestacao = (valorPrestacao * 0.03) + (valorPrestacao* (diasAtrasos * 0.001)) + valorPrestacao
        print(totalPrestacao)
    else:
        totalPrestacao = valorPrestacao
        print (totalPrestacao)
    global valorTotal  
    valorTotal  += totalPrestacao

while valorPrestacao != 0:
    valorPrestacao = int(input("Valor da prestação: "))
    if valorPrestacao == 0:
        print()
        print(valorTotal)
        break  
    diasAtrasos = int(input("Quantos dias de atraso: "))
    valorPagamento(valorPrestacao ,diasAtrasos)




